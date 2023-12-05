import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("facerecogninsmcedsoc-firebase-adminsdk-zi3m9-9d89d0d51f.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://facerecogninsmcedsoc-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

date = {
    "100000":
        {
            "ID":"100000",
            "name":"bilel kort",
            "total_attendance":0,
            "major":"4DS",
            "gender":"male",
            "academic_performance":15,
            "last_attendance_time":"2022-12-11 00:54:34"
        },
     "100003":
            {
                "ID":"100003",
                "name":"aziz mahmoud",
                "total_attendance":0,
                "major":"4DS",
                "gender":"male",
                "academic_performance":15,
                "last_attendance_time":"2022-12-11 00:54:34"
            },
     "100004":
            {
                "ID":"100004",
                "name":"salma turki",
                "total_attendance":0,
                "major":"4DS",
                "gender":"female",
                "academic_performance":15,
                "last_attendance_time":"2022-12-11 00:54:34"
            },


}

for key, value in date.items():
    ref.child(key).set(value)
