# TrailheadBackend

This repo will hold our Django database

## Architecture

Our group is interested in learning more about dev with Django, so we watched this tutorial to understand its architecture: [https://www.youtube.com/watch?v=nGIg40xs9e4&t=103s]([url](https://www.youtube.com/watch?v=nGIg40xs9e4&t=103s))

## Setup

We are using a virtual environment, to get that set up, we navigate to the trailhead folder and used these commands: 
` pip install virtualenv `
`python -m venv myenv`
Then to activate: 
`source myenv/bin/activate`

On Windows: `myenv\Scripts\activate`

To install Django: 
`pip install django`
In order to initialize a Django project within this repo, run this command: 
Next, to download all dependencies: 
`pip install -r dependencies.txt` If there are errors with finding the file specified, ensure you created your virtual environment in the correct folder. 
Then to run the server use this command: 
`python manage.py runserver`

## Deployment

To get the server running: `python manage.py runserver`

you must run `python manage.py makemigrations` then `python manage.py migrate` anytime you make any change to any database models  

UTrek is hosted on render, you can see the backend server setup by following this link: `https://trailheadbackend.onrender.com/`

## Common Errors
1. When getting error `path` not defined in firebase file, go to `\webapp\firebase\firebase_admin.py`, make sure `cred = credentials.Certificate('webapp/firebase/trai-47353-firebase-adminsdk-fbsvc-23759256c6.json')` is uncommented and that `cred = credentials.Certificate("/etc/secrets/trai-47353-firebase-adminsdk-fbsvc-4a91659dff.json")` is commented out. If error persists try comment out the first one and uncomment the second one, though the original setup should work better.

2. If you get an error when running `python manage.py makemigrations`, got to \webapp\migrations and make sure the only python files are 0001_.py through 0008_.py (these are the ones needed). 

Find the file causing the error. If there are additional files casusing issues, type in console: `git rm --cached webapp/migrations/file_name.py`
Any additional .py file should added in .gitignore in this format: `webapp/migrations/file_name.py`
For example, in .gitignore, type: `webapp/migrations/0009_alter_notification_user.py`

## Authors

Ari Rojas
Colin Kearns
Soni Mbesa

## Acknowledgments

## To hardcode a trip into the database
python manage.py shell
from webapp.models import Trip
trip = Trip(info)
trip.save()