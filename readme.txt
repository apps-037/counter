django-admin startproject counter    ------> creates a folder counter with counter folder and manage.py file in it.

You can install the app using manage.py file.

cd counter
python manage.py startapp counterapp  ------> counterapp folder is created with all files in it except urls.py file which we copy from counter folder to this folder.


create static(images, css and js files) and templates(html files) folders in the main counter folder. 
we need to include these three folders into the project so we go to counter -> settings.py and 
         -under INSTALLED APPS we write - 'counterapp' 
         -under TEMPLATES -> DIRS  we write - 'templates'
         -we write STATICFILES_DIRS =  ['static']

then run the server - python manage.py runserver

 then we need to make urls to display the contents accordingly
go to urls.py and make path('helloworld/', )
                                  |
                                  |___ path from where to call the html file 

create a folder in templates folder called helloworld and create a file in it helloworld.html and type the code in tht html file.
then go to views.py --------->      


			from django.shortcuts import render

			# Create your views here.		
			def helloworld(request):
				return render(request, "helloworld/helloworld.html");            //renders request to request the html file from helloworld folder 



then go to urls.py in the counterapp folder ------->

                                 
			from django.contrib import admin
			from django.urls import path
			from .views import helloworld                                //the helloworld function is imported from views

			urlpatterns = [
			    path('helloworld/', helloworld ),                        //the path and the function to be called is specified
			]


after this try running server it doesnt run because the urls are not recognized in the project but only in the app for that we go to the folder of counter and 
urls.py in which we include   ------------->


			from django.contrib import admin
			from django.urls import path, include

			urlpatterns = [
			    path('admin/', admin.site.urls), 
			    path('', include('counterapp.urls'))
			]
 

we make hellostudent file in the same way and render it
now in both files the html code is getting repeated so loads again and again to increase efficiency we alter the code in this way by making a common file base.html -------->

		base.html
	
				<!DOCTYPE html>
				<html lang="en">
				<head>
				    <meta charset="UTF-8">
				    <meta http-equiv="X-UA-Compatible" content="IE=edge">
				    <meta name="viewport" content="width=device-width, initial-scale=1.0">
				    <title>hello</title>
				</head>
				<body>
				    {% block content %}
    
				    {% endblock %}
				</body>
				</html>


				
		helloworld.html

				{%  extends 'base.html' %}

				{% block content %}
				<h1 style="color: red;">Hello world!!</h1>

 				   {% endblock %}



PASSING PYTHON VARIABLES TO THE TEMPLATES - 

For passing variables we make a dictionary which is passed in the render request. 


































