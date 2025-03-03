import firebase_admin
from firebase_admin import credentials, firestore


import os
print("Current working directory:", os.getcwd())




# Path to your service account key file
cred = credentials.Certificate('webapp/firebase/trai-47353-firebase-adminsdk-fbsvc-4a91659dff.json')

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred)


# Initialize Firestore
db = firestore.client()  # This is your Firestore database reference