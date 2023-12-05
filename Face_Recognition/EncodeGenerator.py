import cv2
import pickle
import os
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

bucket_name = "facerecogninsmcedsoc.appspot.com"


cred = credentials.Certificate("facerecogninsmcedsoc-firebase-adminsdk-zi3m9-9d89d0d51f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecogninsmcedsoc-default-rtdb.firebaseio.com/",
    'storageBucket': bucket_name
})

# importing student images
bucket = storage.bucket()

folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)

imgList = []
studentIds = []

# Iterate over the files in the folder
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'

    # Create a blob reference within the bucket
    blob = bucket.blob(fileName)

    # Upload the file to Firebase Storage
    blob.upload_from_filename(fileName)

    print(f"Uploaded {fileName}")

print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encodeing Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
# print(encodeListKnown)
print("Encoding Completed")

file = open("EncodeFile.p", 'wb')           #pickel file
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")


