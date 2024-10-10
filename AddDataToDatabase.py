import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionrealtime-589f7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "13322":
        {
            "name":"Deepak Jangra",
            "major":"Software Engineer",
            "starting_year": 2023,
            "total_attendance":10,
            "standing":"G",
            "year":2,
            "last_attendance_time": "2024-08-06 00:54:34"
        },

    "963852":
        {
            "name":"Elon Musk",
            "major":"Research",
            "starting_year": 2022,
            "total_attendance":10,
            "standing":"E",
            "year":3,
            "last_attendance_time": "2024-08-06 00:54:34"
        },

    "852741":
        {
            "name":"Emly Blunt",
            "major":"Economics",
            "starting_year": 2021,
            "total_attendance":10,
            "standing":"A",
            "year":4,
            "last_attendance_time": "2024-08-06 00:54:34"
        }
}



for key,value in data.items():
    ref.child(key).set(value)

