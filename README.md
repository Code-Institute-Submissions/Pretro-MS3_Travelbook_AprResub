#__Travel Journal__

(https://ms3-traveler-project.herokuapp.com/)

The goal of this project is to give users the opportunity to keep a journal about the places they have been to and visited. This is possible by register and making a user profile. The user then will be able to create, update and delete it's own stories. Also there is the possibility to read about other users stories. In the making of this project CRUD functionality where included programmed in python.

In future updates of this project, it is intended to expand the profile of the user giving it the ability to upload pictures from places they have been and a profile picture. To protect the integrity of the user, as a security measure, the information shown as the name and picture profile, will only be available to register users.

This is the third project out of four Milestone Projects at the Code Institute for the Full Stack Development Course.

# User Experience __(UX)__

## __User stories__

As a user of this site, I want to

1. As a user, i want to be able to understand what the site is about so that i can decide if this is a site of my interest.

2. As a user, i want to easy navigate through the different pages so that i can use the site.

3. As a user, i want to register an account so that i can become a member.

4. As a user, i want the process of registration to be simple so that i can start make use of the site and not lose interest with registration processes that take a long time.

5. As a user, i want to easily log in so that i can start using the website at once.

6. As a user, i want to manage my travel journal information easily so that it can be time efficient.

7. As a user, i want to be able to add travel journal stories so that i can share my stories with others.

8. As a user, i want to read other members travel journal stories so that i can compare it with mine journal stories.

9. As a user, i want to search other members travel journal stories so that i can see where the most popular travel destination are.

10. As a user, i want to comment other members travel stories so that i can follow up others stories and compare with mine stories.

11. As a User, i want to chat with other members so that i can communicate with them.

## __The purpose of the travel journal is to :__

+ Create a community where people from all around the world can meet and interact.

+ A fun way to write your stories and adventures and share it with others.

+ Give us the possibility in these difficult times to get a little closer and make life a little more entertaining.

The idea was born during the pandemic. It is believed that interest in travel will increase markedly after this difficult time is over. Choosing a destination is not always easy, but through a page where you can search for destinations and integrate with other travelers, 

check their comments and reviews of the different places they have been to, in some way it makes it easier to choose where you would like to travel to in the future.

### __Project Strategy__

To meet the goal of this project, the following strategy has been implemented.

+ Provide CRUD functions are included making it possible for the user to handle their information.

+ The site is built to easy navigate and this makes it also easy to use.

+ Implemented messages that keep the user informed of every action they made.

+ The use of photos that is in accordance with the objective of the site, making an environment pleasant for the user.

+ The travel journal stories written by the users are available for everyone to read and leave a comment.

### __Design__

__Color Scheme__

The colours that I used for the site:

* (Yellow) For the main color of the buttons, the logo, icons and the h1, h3 titles. 

* (Orange) For the hover effect on the buttons.

* (Black) Is used for the text shadows.

* (White) Is use for the menu options in the navbar and for the paragraph in the home , log in and register, add and edit adventure page textfields .

* (Lightgrey) Is used for background forms in all of the sites pages.

* (Green) is the default color of the icon in the comment feature.

The reason why these colors were chosen is because since the background image is colorful, these colors give a more joyful tone and at the same time allow the user to be focused on what they are doing. Generating a more attractive effect not only for the frequent user but also for the one who visits the site for the first time.
    
### __Typography__

"Roboto" and Sans-Serif font has been used in the website. The reason why this font was chosen is because it makes the text of the site more clear. Roboto has a dual nature. It has a mechanical skeleton and the forms are largely geometric. Roboto also allows letters to be settled into their natural width. This makes the reading rhythm to be more natural.
    
### __Imagery__

The only image used in this project is the background image of the main page. The reason for this is because the project is more focused on fulfilling the function of a journal, for which it was not necessary to create a carousel or other type of features related to images.

In the future it is planned to make an application that allows users to upload profile photos and also add photos to their travel stories.

## __Wireframes__

+ [Wireframe 1](/static/wireframes/home.png)

+ [Wireframe 2](/static/wireframes/adventure.png)

+ [Wireframe 3](/static/wireframes/login.png)

+ [Wireframe 4](/static/wireframes/profile.png)

+ [Wireframe 5](/static/wireframes/register.png)

+ [Wireframe 6](/static/wireframes/responsive.png)

+ [Wireframe 7(/static/wireframes/edit_adventure.png) ]

## __Features__ 

* Responsive on all devices.

* Interactive elements.

* Responsive navbar.

* Designed with HTML5, CSS, Python3, JavaScript, Flask,Materalize, and MongoDB.

* Alert messages that inform the user about the different operations carried out in the system.

* Register page where users can register to make use of the website.

* Login page where only register users can have access to.

* Modal for users to write the information about to their travels.

* Buttons for the operations of add, update, delete, search, login and register functions.

* Cards where registered members such as site-only visitors can leave comments about registered members travel stories.

## __Features left to implement in the future__

* A function that makes it possible to recover user password.

* The upload of pictures to the profile section. 

* The making of photo albums so that every user can share their experience with others with pictures.

* A chat channel for all members to communicate.

* A map where the user can mark the cities and places he/she has visited.

## __Technologies Used__

+ For the making of this project, the following technologies has been used__

##### __Languages__

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [Python](https://www.python.org/)

##### __Library__ 

* [jQuery](https://jquery.com/)   

  jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling and CSS animation.

#### __Database Used__ 

* [MongoDB](https://www.mongodb.com/3)

  MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.

#### __Integrations__

+ [Fontawesome](https://fontawesome.com/)

  Font Awesome is a font and icon toolkit i use for the icons on different pages.

+ [Flask](https://flask.palletsprojects.com/en/1.1.x/)

  Flask is a micro web framework written in Python. It is classified as a microframework because it does not need particular tools or libraries. 

+ [Googlefonts](https://fonts.google.com/)

  Used in this project for typography.

+ [Materialize](https://materializecss.com/)

  Materialize is a modern responsive CSS framework based on Material Design by Google.

### __Repository, workspace__

+ [Gitpod](https://www.gitpod.io/) 

  Gitpod is used as the enviroment program were the page was made and for the writing of the code.

+ [Github](https://github.com/) 

  I use Github to host the deployed website. Also in Github you can track your code and go back to previous versions to keep track of what you've done.

+ [Heroku](https://www.heroku.com/)

  Platform used for the deployments and running the apps. 

## __Resources__
 
+ [Balsamic](https://balsamiq.com/)

  Program use for the making of the wireframes for this project.

+ [YouTube](https://www.youtube.com/)

  I use this site to get inspiration from other projects and to search information about source code. 

+  [Markdown](https://guides.github.com/features/mastering-markdown/)

  Markdown is a easy-to-use syntax for styling all forms of writing on the GitHub platform.

+  [W3schools](https://www.w3schools.com/)

  I use this site to get answers to questions about the programming languages used. 

## The code is validated in the following pages for error correction:

+ [W3C Validator HTML](https://validator.w3.org/)

+ [JSHint](https://jshint.com/)

+ [CSS](https://jigsaw.w3.org/css-validator/#validate_by_input)

+ [Pep8](http://pep8online.com/)

+ [Reposinator](https://www.responsinator.com/)

+ [Devtool](https://developers.google.com/web/tools/chrome-devtools)

# Data schema

+ MongoBD was used for the making of the datasbase.

The collections are:

 __Continents__ 

Title |  Db Key | Data Type | 
----- | ------- | --------- | -
User id | _id | ObjectId 
Continent | continent|String

__Profile__ 
Title |  Db Key|Data Type | 
------------|-|-|-
User_id | _id | ObjectId
Username |username|String

__Travels__ 
Title |  Db Key|Data Type | 
------------|-|-|-
User_id | _id | ObjectId
Continent | continent | ObjectId
Country | country | String
City | city |String
Date of travel | date | String
Description | description | String
by | created_by | ObjectId
Comments: | comments | Array

__Users__ 
Title |  Db Key|Data Type | 
------------|-|-|-
User_id | _id | ObjectId
Username | username | String
Password | password | String

 + The Users id is connected to all the collections in order to know who the data belongs to.

 + the variable username in the collection of profile and user allows verification when creating a new record and also verification that the same username is not entered twice.


## Testing

    During the testing time, the following code validates are use. It is worth mentioning that there were errors in the html code due to the content blocks written in jinja. After talking to my mentor, he has informed me that this is normal.

+ [W3C](https://validator.w3.org/) Validator HTML.

+ [W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) validator CSS.

+ [Pep8](http://pep8online.com/) validator Python

+ [JSHint](https://jshint.com/) JavaScript

## __Testing User Stories from User Experience (UX) Section__ 

1. As a user, i want to be able to understand what the site is about so that i can decide if this is a site of my interest.

    i. When entering the page, it presents a title, a paragraph in which it is clearly read what the site is about. Background photography also helps to understand the purpose of the page.

2. As a user, i want to easy navigate through the different pages so that i can use the site.

    i. The main page has a navigation menu in which there are two options, one for log in and the other for registration. Once the user is registered, the remaining options shows on the navmenu and this makes the navigation on the site possible for registered users.

3. As a user, i want to register an account so that i can become a member.

    i. The user has the option of registering a user account in the navigation menu. Once this is done, the user is a registered member.

4. As a user, i want the process of registration to be simple so that i can start make use of the site and not lose interest with registration processes that take a long time.

    i. To registrate choose a username of your choice and a password. Then you can start using the site. This process avoids a delayed registration process and that the user loses interest in the site.

5. As a user, i want to easily log in so that i can start using the website at once.

    i. Like the registration process. The login process also consists of filling in the username and password already registered by the user.

6. As a user, i want to manage my travel journal information easily so that it can be time efficient.

    i. The system is made in such a way that the user can input, edit and delete their information from different points of the system through a navigation menu and links.

7. As a user, i want to be able to add travel journal stories so that i can share my stories with others.

    i. Once the user is logged in, by pressing the adventure tab option in the navigation menu, the user is directed to the add adventures page.

    ii. Once the information is entered, it is displayed on the main page where it is available for both visitors and members to read.

8. As a user, i want to read other members travel journal stories so that i can compare it with mine journal stories.

    i. In the home page the stories of other members are shown on cards. This makes it possible to read and compare the stories with the users own experiences.

9. As a user, i want to search other members travel journal stories so that i can see where the most popular travel destination are.

    i. .In the search section, choose the destination you are looking for, the information will appear on the page in the cards written by the users who have visited the place you are looking for.

    ii. It should be clarified that at the moment it is only possible to search by "country"

10. As a user, i want to comment other members travel stories.

    i. Upon entering the system, a modal is displayed where the travel history cards of the members appear. By clicking on the comments option it is possible to leave a comment whether you are a visitor or a member of the page.

11. As a User, i want to chat with other members.

    i. This option is not available at the moment, but it is a project to be carried out in the near future.

* During my test period i focus on the user stories.

# __Further Testing__

## The testing of the Navbar and pages. 

### __Adventure Page__

+ Test result: The user was directed to the login form when pressing the option "Log in" in the navbar. 

+ Test result: The user was directed to the register form when pressing the option "Register" in the navbar.

+ Test result: The user was able to make a search for country successfully in the search form.

+ Test result: The alert messages in the search form worked as expected.

### __Log in__

+ Test result: The user could log in by writing his user information in the login form.

+ Test result: The user could register by filling the register form.

+ Test results: Alert messages were triggered when a non existing user was tested.

### __Register page__

+ Test result: The user could register in the register form.

+ Test result: Alert messages were triggered when trying to register an existing user.

### __The adventure page__

+ Test result: The user was directed to the adventure page when pressing the "Adventure" option in the navbar.

+ Test result: The user could add information successfully in the Add adventure form.

+ Test result: Alert messages were triggered during the "Add adventure" fields test. This means, leave a field blank and try to make an entry of information.

+ Test result: The add button worked as expected. alert messages triggered when trying to add incomplete information written in the adventure form. 

### __Edit Adventure page__

+ Test result: The user could edit information successfully in the edit adventure form.

+ Test result: Alert messages were triggered during the "Edit adventure" fields test. The result was the same as mentioned above, only this time the operation was editing information. 

### __Profile page__

+ Test result: The warning modal is activated when the delete button is pressed.

+ Test result: The user is directed to the edit adventure page when pressing the edit button.
    
### __The website has been checked in different browser, such as.__

1. Chrome

2. Firefox

3. Safari

4. Microsoft edge

* The responsive part has also been tested in http://www.responsinator.com/ for

1. Ipad

2. Iphone

3. Android

4. Laptop

Friends and family tested the site by login in and writing about their stories. This was also made to point out any bugs and/or user experience issues.

## __Known Bugs__

+ 

## __Deployment__ 

To deploy this project, I used the hosting platform of Github and heroku. The step to deploy this project are as follows.

+ GitPod is used for the creation of this project.

+ GitHub was use for the creation of the project repository. 

+ The repository is connected to Gitpod. All the changes during the creation of the project are commited and push to GitHub.

+ As a final part,  the project is deployed to heroku. This is achieved by the linking between github and heroku.

### __Heroku__

The Project is deployed to Heroku using the following steps...

 1. Navigate to [Heroku](https://www.heroku.com/) and log into your account.

 2. Press the "new" button in the dashboard and choose "Create new app" option.
 
 3. Write you apps name and choose the region according to where you live. 
 
 4. Then press the "create app" button.
 
 5. Press the "Settings" tab. Once done, you see the "config vars" section in the screen.
 
 6. Press the "Reveal Config Vars" button and add your configuration variables created in the env.py file.
 
 7. The config var are the IP, PORT, Secret Key, Mongo_URI, MongoDB.
 
 8. Once this is done, choose the "Deploy" tab in the menu.
 
 9. In the "Deployment method" section, choose the "Github" icon and connect your Github repository.

10. Be sure to choose the right GitHub username and search for the repository you want. This you can do with the search option.

11. Press the "Disable Automatic Deploys" button to change it to "Enable Automatic deploy" mode.

12. Press the "Deploy Branch" button.

### __Forking the GitHub Repository__ 

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

+ Log into your GitHub account.

+ Search for the repository you want to create a fork, in the search section at the top left of the screen.

+ Once chosen, just above the "Settings" tab on the menu, at the top right of the screen, locate the "Fork" Button.

+ Press the "Fork" button.

+ You should now have a copy of the original repository in your GitHub account.

### __Local Deployment__

1. On GitHub, navigate to the main page of the repository.

2. Above the list of files, click "Code".

3. Mark the HTTPS tag ad press the copy icon at the end of the link.

4. Open Git Bash

5. Change the current working directory to the place where you want the cloned directory to be made.

   Type  "git clone", and then paste the URL you copied.

    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

6. Press enter and you should see the following code on the screen

    ![example image of git clone](images/git-clone.png)

7. Open the index.html in the folder that you clone the project.

### __Credits__

__Code__

* [Materialize](https://materializecss.com) 

+ Library used throughout the project in the making of the website and to make it responsive.

* [Online Tutorials](https://www.youtube.com/watch?v=enBAFo2kEfE)

+ For the use of button effects and other features of the site. I search information from Open tutorials

* [Websolutions](https://www.websolutions.com/blog/7-of-the-most-common-website-errors-and-what-they-mean/)

+ I use this site to get information about the website errors encounter in this project.

__Content__

+ I use the mini project tutorial from Code Institute as a guidance in the making of this project. 

+ Part of the code written is my code and ideas and guidance from my mentor Antonio Rodriguez.

__Media__

All Images are from the following site:
+ [Pexels](https://www.pexels.com/sv-se/)

__Acknowledgements__

+ My Mentor Antonio Rodriguez for continuous helpful feedback.

+ Tutor support at Code Institute for their support and help.

+ My friend Christian Mossberg for guidance and support.

+ My dear friend and journalist Maria Hagström for support with her travel stories and testing this site as a user.

+ Tim Nelson for tutorial from Code Institute that i use for guidance in this project.
