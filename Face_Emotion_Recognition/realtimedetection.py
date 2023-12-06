import cv2
from keras.models import model_from_json
import numpy as np
import csv
import time

# Load the model
json_file = open("facialemotionmodel.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("facialemotionmodel.h5")

# Load the face cascade classifier
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Define the function to extract features from an image
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

# Open the CSV file for writing
csv_file = open("detections.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Face", "Emotion"])

webcam = cv2.VideoCapture(0)

labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

prev_time = time.time()
detection_interval = 1  
while True:
    # Read a frame from the webcam
    ret, im = webcam.read()
    if not ret:
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Check if enough time has passed for the next detection
    current_time = time.time()
    if current_time - prev_time >= detection_interval:
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(im, 1.3, 5)

        try:
            for (p, q, r, s) in faces:
                # Extract the face region
                face_image = gray[q:q+s, p:p+r]

                # Resize the face image to the required size
                resized_image = cv2.resize(face_image, (48, 48))

                # Extract features from the resized image
                features = extract_features(resized_image)

                # Make a prediction using the model
                pred = model.predict(features)
                prediction_label = labels[pred.argmax()]

                # Draw the bounding box and label on the original image
                cv2.rectangle(im, (p, q), (p+r, q+s), (255, 0, 0), 2)
                cv2.putText(im, prediction_label, (p-10, q-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255))

                # Write the detection to the CSV file
                csv_writer.writerow([f"Face {len(faces)}", prediction_label])

            # Update the previous detection time
            prev_time = current_time

        except cv2.error:
            pass

    # Show the output image
    cv2.imshow("Output", im)

    # Exit if 'Esc' is pressed
    if cv2.waitKey(1) == 27:
        break

# Close the CSV file and release the webcam
csv_file.close()
webcam.release()
cv2.destroyAllWindows()