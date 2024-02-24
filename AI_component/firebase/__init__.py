import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/workspaces/AI_component/eager2learn-fc8bd-firebase-adminsdk-1o689-a9df071717.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://eager2learn-fc8bd-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/')
print(ref.get())