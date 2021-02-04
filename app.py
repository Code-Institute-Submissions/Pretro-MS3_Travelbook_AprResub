import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Configuration to grab the DB name
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")

# Congifure the actual connection string
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Grab the secret key
app.secret_key = os.environ.get("SECRET_KEY")


# We setup an instance of Pymongo and add the app using a constructor method
mongo = PyMongo(app)

@app.route("/")
@app.route("/travel")
def travel():
    return render_template("traveling.html", travel=travel)


# Reg_user function
@app.route("/reg_user", methods=["GET", "POST"])
def reg_user():
    if request.method == "POST":
        # check if the username exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists,try another name")
            return redirect(url_for("reg_user"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("reg_user.html")


# Log in function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Checks if there isan existing user
        if existing_user:
            # Checks the password to match user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)