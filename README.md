# Restaurant landing page and online ordering system 
_by Jianhui Huang_ [(jian.huanghe@gmail.com)](mailto:jian.huanghe@gmail.com?subject=[Github]%Source%20Han%20Sans)

## Content
1. Project description 
1. Implementation
1. Programming journey
1. Features
1. Afterthoughts
___
* How to launch the App
* How to deploy the App with Google Cloud Platform

## Project description
This project was the final assignment for an introductory programming course. The course can be found [**here**](https://github.com/DominiquePaul/DSCS2020). As such this was my first time personally developing and deploying a somewhat complete online web application with python. 

The aim of this project was to create a basic restaurant website with adeqaute styling and some useful functionalities. The idea originated simply from the fact that I knew some acquaintances that had a restaurant but no online website yet. Since so far I´ve only been on the user-end of websites, I thought that it might also be interesting to see how I myself would approach designing a website.

**SPOILER: It did _not_ turn out the way I wanted it to be.**  


## Programming journey

In a first session I´ve quickly created a flask-app with all the necessary html templates. So far it was only about the styling. Then after bascically not working on this project for a few weeks, I came back and wanted to add the functionalities. Unfortunately, I had forgotten many of the learned basics or at least I always found myself getting stuck on small and unnecessary mistakes. Thus this kind of led me to lose some interest and motivation for this project. Adding to all this, I just wasn´t able to make a flask admin dashboard work with the ordering system. Following some youtube/stackoverflow research during this time, I was made aware that the django framework already had an easy-to-use admin dashboard included. Because I, out of curiosity, had already looked at some django documentation and because I was pretty much stucked with flask, I just gave it a shot and went through some django tutorials, which eventually worked out. 

To sum it up, the app is actually made of two separate apps that link to each other. One is developed with the flask and the other with the django framework. 
While one of the assignment requirement was for the project to be developed with flask, I hope this is still somehow acceptable. 


## Features 
**The application offers**
* styled restaurant pages with basic informations (home, menu, contact, about, order)
* the customers the options to online reserve a table, order takeout and pay
* the admin an dashboard where one can create, read, update and delete items from the application

*(Note: Names, addresses and locations were anonymized for privacy reasons.)* 

### Technical aspects
* reservation email is send via smtp´s gmail server
* Payment feature was implemented with AJAX
* data is stored with django´s default SQLlite database
* the admin dashboard is created with django´s default admin site
* most of the actual code is very messy since I´ve added and deleted things very irregularly to the point I dont even know where some things are

## Afterthoughts
I had quite some difficulties with this project. The main problem was that I took quite a long pause from programming after the lectures ended and hence also forgot many things. This led to me being constantly frustrated because I had to look a lot of things up again. This in turn led to me losing motivation and at this point I just wanted to be done with this project.

## How to launch the App

* Requirements: python3, flask, django and pip installed
* I did not work with venv, requirement.txt file or environmental variables so the steps required to get everythin running are a bit inconvenient

### Flask-App
1. Download the "flask_app" folder and unpack it
1. Open the folder in your IDE 
    1. Open /templates/base.html and insert your Google Maps API Key. You can get one for free following this [guide](https://developers.google.com/maps/documentation/javascript/get-api-key)
    1. Open /main.py, go to the "contact" route and insert your Gmail email and password
1. Try to run main.py (You will most likely get an error because of missing packages)
    1. Repeat until main.py works: Try to run the app, see which packages are missing and install all missing packages

### Django-App
1. Download the "django_app" folder and unpack it
1. Open the folder in your IDE 
1. Try to run manage.py in windows powershell (You will most likely get an error because of missing packages)
    1. Repeat until manage.py works: Try to run the app, see which packages are missing and install all missing packages
    
* Login for /admin = Username: "admin"; password="heuteistmontag"

## **Resources:**
* Django: [Basic series by Corey Schaefer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1)
* Django: [Ordering system](https://github.com/lobsterick/pinocchio_pizzeria)
* Django: [django_allauth templates](https://github.com/pennersr/django-allauth/tree/master/allauth)
* [PayPal payment with AJAX](http://legionscript.com/articles/20/)
* [Google Maps API](https://developers.google.com/maps/documentation/javascript/markers#maps_marker_simple-javascript)
