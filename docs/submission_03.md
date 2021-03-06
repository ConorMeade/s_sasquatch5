# SASQUATCH 5

# UMASS VULTURES

# Overview
For this project we added models, views, and a button on the Navbar for the Maps page. This will be part of our final submission where we will have all the food posts be visible on a map of the UMass campus.

Also, we implemented a working form for a food post that will ask a user the food, location, start/end time, and a description. We will parse this form and add it to our database to be viewed on the admin site a well as in our feed. Similarly, we implemented a form for registering a user. A new user will provide a username, password, and password confirmation and then be added to the user database.

Lastly, we have a login/logout functionality. Logged out users will still be able to view posts, comments, and the map. Logged in users will be the only ones able to make posts/comments however. Also, there will be slight differences in how our app pages are viewed based on whether a user is logged in or not. We also have a set of superusers that can make special adjustments on the site admin page.

# Team Members

* Conor Meade, Github ConorMeade
* Abhaydeep Singh, Github Ab-hay
* Parth Goel, Github Parth-03
* Garrison Qian, Github GarrisonQian
* Thomas Bui, Github thomasbui1997

# Video Link
https://youtu.be/70oaokJIBHQ


# Design Overview
For the login/logout functionality of our project, if a user is not logged into an account, they will be given an option of registering to create an account. This 'Register' page is a form that when filled out will give the user the privileges of a logged in user as well as add the new user to the site database. We also have a 'Members View' page where users can go down the list of users and see the specific posts, comments, and score of that user. This is useful for if someone has a preferred user or has had good experiences with the food options a certain user has given before. The 'Member's View' page is only available to logged in users; if a logged out user tries to access this page, they will be prompted to "Please login first".

For ease of logging in, we simply made the log in form part of our Navbar so users will not have to navigate to a new page rather they can seamlessly log in. New data in the form of food posts can be added by going to the 'Post' tab, filling out the form and then the post will appear on the 'Feed' tab where users can upvote/downvote posts and make comments.

Users can now create new posts on the 'Post' page. They must provide the time, location, and description of relevant events. If the original poster is logged in when they create the post, their username will be displayed on the post. These posts are added to the feed. 

On the feed, each post has a 'Poster' field which displays the author of the post. If the author was not logged in when they made the post, this field will be set to 'None'. The time, location, and description will be shown as the author provided. The score will initially have a default value of 0. Users will only be able to modify and delete posts when they are logged in and viewing their own posts. 


# Problems/Successes
For successes, we were able to implement the login/logout functionality pretty seamlessly in our Navbar. Also, creating different views for a logged in user and logged out user was pretty easy and allowed for better control over what privileges users of the app have. Also we were pretty ahead on this project as we implemented login/logout pretty far in advance so the only major hurdle we had for this project was getting the forms working correctly.

As for problems for this project, getting the forms and feed to work was a challenge. Parsing the form and adding that data to our database was something that was an issue for a little bit but we were able to figure it out. We also struggled with the group portion of the project and figuring out how to differentiate from users and groups.

# Team Choice
For our final submission, we will work on the functionality for the map portion of our project. This will mean taking all the post in the feed and making them visible on an interactive map of the UMass campus. 

We will also work on different visual aspect of our app including color schemes, more extensive profile pages, and adding more details to our forms so we can have more descriptive posts. Basically adding CSS elements to our site to spruce it up.

Lastly, we will implement a working comment form to give users an opportunity to give feedback on a post.