from django.db import models

# Django provides an object relational mapping (ORM)
# allows us to write python code to create database models and 
# then those models are AUTOMATICALLY created for us in SQL light 3 
# we make a migration, which is automated code, which creates the corresponding model in SQL or mongoDB

class TodoItem(models.Model): 
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

from django.db import models
#defines the structure of our data, 
#specifying fields / attributes and 
# types like strings, integers, dates
# Models in Django map to database tables
# so each instance of a model is a row in that table.
class Trip(models.Model):
    title = models.CharField(max_length=100)
    tripLeader = models.CharField(max_length=100)
    date = models.DateField()
    #attendees = models.CharField(max_length=13, unique=True)
    #TKTK will be fleshed out with colin's data base info 

    def __str__(self):
        return self.title
    
    #trip registration ID  
    #student ID 