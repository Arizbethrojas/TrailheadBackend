import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

import os
print("Current working directory:", os.getcwd())




# Path to your service account key file
# load_dotenv()
# api_key = os.getenv('FIREBASE_KEY')
# url = 'webapp/firebase/' + api_key
#render stores this in the root file
cred = credentials.Certificate("/etc/secrets/trai-47353-firebase-adminsdk-fbsvc-4a91659dff.json")


# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred)


# Initialize Firestore
db = firestore.client()  # This is your Firestore database reference
