#here is where we will place different URL routes and then connect them to our views 
from django.urls import path 
from .views import TripCreate
from . import views

# list of our paths
urlpatterns = [
    path("", views.home, name ="home"), #this is an empty path to the base URL of our website
    path("todos/", views.todos, name = "Todos"),
    path('api/trips/', TripCreate.as_view(), name='trip-create'),
]