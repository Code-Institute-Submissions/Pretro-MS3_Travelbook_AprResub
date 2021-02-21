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
@app.route("/adventure")
def adventure():
    travels = list(mongo.db.travels.find())
    for travel in travels:
        try:
            continent_name = mongo.db.continents.find_one(
                {"_id": travel["continent"]})
            user_name = mongo.db.users.find_one({"_id": travel["created_by"]})
            travel["continent"] = continent_name["continent"]
            travel["created_by"] = user_name["username"]
        except Exception as e:
            print(e)
            pass
    return render_template("adventure.html", travels=travels)


@app.route("/add_adventure", methods=["GET", "POST"])
def add_adventure():
    if request.method == "POST":
        continent = mongo.db.continents.find_one(
            {"continent": request.form.get("continent")})
        user = mongo.db.users.find_one({"username": session["user"]})
        traveler = {
            "continent": ObjectId(continent["_id"]),
            "country": request.form.get("country"),
            "city": request.form.get("city"),
            "date": request.form.get("date"),
            "description": request.form.get("description"),
            "created_by":  ObjectId(user["_id"])
        }
        mongo.db.travels.insert_one(traveler)
        flash("Travel destination ready!")
        return redirect(url_for("adventure"))

    continents = mongo.db.continents.find().sort("continent", 1)
    return render_template("add_adventure.html", continents=continents)


# Edit adventure
@app.route("/edit_adventure/<adventure_id>", methods=["GET", "POST"])
def edit_adventure(adventure_id):
    if request.method == "POST":
        continent = mongo.db.continents.find_one(
            {"continent": request.form.get("continent")})
        user = mongo.db.users.find_one({"username": session["user"]})
        enviar = {
            "continent": ObjectId(continent["_id"]),
            "country": request.form.get("country"),
            "city": request.form.get("city"),
            "date": request.form.get("date"),
            "description": request.form.get("description"),
            "created_by": ObjectId(user["_id"])
        }
        mongo.db.travels.update({"_id": ObjectId(adventure_id)}, enviar)
        flash("Information Updated Successfully")

    traveler = mongo.db.travels.find_one({"_id": ObjectId(adventure_id)})
    continents = mongo.db.continents.find().sort("continent", 1)
    return render_template("edit_adventure.html", traveler=traveler,
                           continents=continents)


# Delete function
@app.route("/delete_adventure/<adventure_id>")
def delete_adventure(adventure_id):
    mongo.db.travels.remove({"_id": ObjectId(adventure_id)})
    flash("Adventure deleted")
    return redirect(url_for("adventure"))

# Search function


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    travels = list(mongo.db.travels.find({"$text": {"$search": query}}))
    return render_template("adventure.html", travels=travels)


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
            "password": generate_password_hash(request.form.get("password"),
                                               ),
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


# Log out function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("Goodbye, Have a nice travel!")
    session.pop("user")
    return redirect(url_for("login"))


# Profile function
@app.route("/globetrotter/<username>", methods=["GET", "POST"])
def globetrotter(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    user_travels = list(mongo.db.travels.find({"created_by": username["_id"]}))
    for travel in user_travels:
        continent_name = mongo.db.continents.find_one(
            {"_id": travel["continent"]})
        user_name = mongo.db.users.find_one({"_id": travel["created_by"]})
        travel["continent"] = continent_name["continent"]
        travel["created_by"] = user_name["username"]
    if session["user"]:
        data = {"username": username["username"], "user_travels": user_travels}
        return render_template("globetrotter.html", data=data)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
