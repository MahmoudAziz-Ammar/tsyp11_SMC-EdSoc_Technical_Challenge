Team members : 
-Bilel Kort 
-Mahmoud Aziz Ammar
-Salma Turki


# 1- Analysis Part

## Analysis
The Analysis folder contains essential files and datasets for studying well-being in the project. This folder serves as a central hub for analyzing and exploring the data related to well-being on both local and Global scales.

## File Structure
The folder consists of the following files:

-Local Dataset (xlsx file): This dataset focuses on well-being indicators at the local level. It contains relevant data points and variables specific to the local context, providing insights into well-being trends within a specific geographic area.

-Global Dataset (CSV file): This dataset encompasses well-being indicators at the Global level. It includes data from various countries, allowing for comparative analysis and identification of global well-being patterns.

-Local Well-being Analysis (Google Colab Notebook): This notebook is specifically designed for analyzing the local dataset. It provides a computational environment and code resources for exploring, visualizing, and performing statistical analyses on the local well-being data.

-Global Well-being Analysis (Google Colab Notebook): This notebook is dedicated to analyzing the Global dataset. It offers a similar computational environment and code resources as the local analysis notebook, but tailored for the Global well-being data.

## Purpose
The Analysis folder and its accompanying files aim to facilitate a comprehensive examination of well-being factors. Researchers and contributors can utilize the datasets and analysis notebooks to gain meaningful insights into the well-being trends at both local and international levels. The provided resources enable data exploration, visualization, and statistical analysis, empowering users to draw evidence-based conclusions and contribute to the overall understanding of studying well-being.

Feel free to explore the files and leverage the provided tools to conduct your analysis effectively. For further instructions on how to use the files and reproduce the results, please refer to the individual README files within each file's directory.

Note: It is essential to acknowledge the original sources and cite the datasets used in your analysis to ensure proper attribution and compliance with any licensing requirements

# 2- Dashboard 

This repository contains a comprehensive and visually appealing Power BI dashboard designed to showcase collected data in a meaningful and interactive manner
The dashboard provides an easy-to-use interface, allowing eductaors and administration to explore and analyze data effortlessly. It incorporates two sets of screenshots, each capturing a different aspect of the dashboard's functionality.

The first set of screenshots presents general information about the institution, such as the number of complaints, student enrollment, and other relevant metrics. These visuals offer a high-level overview of the institution's performance and key indicators.

The second set of screenshots focuses on specific information related to mental health, physical health, and social indicators. These visuals provide deeper insights into these critical areas, allowing stakeholders to identify trends, patterns, and potential areas for improvement.

Additionally, this repository includes an HTML file that demonstrates a local deployment of the Power BI dashboard on our faculty's Esprit website. This deployment showcases the accessibility and practicality of the dashboard, enabling users to access and interact with the data directly from the website.

also, dashboard_solution.xls is an exemple of dataset to use it into the dashboard.

NB : This repository contains a visually appealing Power BI dashboard showcasing collected data. Please note that direct access to the live dashboard requires a Power BI Pro account. However, we have provided a video capture demonstrating the dashboard's functionality and features. Feel free to watch the video to explore the dashboard's capabilities.

# 3- Face Recognition with Real Time

## Description

This project leverages Python and OpenCV to implement real-time face recognition capabilities. It utilizes Python 3.7, higherOpenCV, cvzone, numpy, face_recognition, and the Firebase Admin SDK to achieve accurate and efficient face recognition in various real-time scenarios.

## Sample Output
![Capture d'écran 2023-12-04 115114](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/6da22082-41c6-4778-9fc4-ae1cebc7e354)

## Real Time Database

The development of a real-time face recognition system requires the integration of advanced facial recognition algorithms with a live camera feed. To achieve this, a seamless connection to a Firebase real-time database is established. This enables the system to upload scanned faces dynamically, ensuring efficient storage in the database while simultaneously updating attendance records. As individuals are recognized in real-time, their corresponding photos are securely stored in Firebase storage, providing a comprehensive solution for accurate attendance tracking.

The implementation of real-time face recognition involves the integration of a system that seamlessly connects to a live database, such as Firebase. When faces are scanned in real-time, the captured images are instantly uploaded to the Firebase database, ensuring a swift and efficient storage process. At the same time, the attendance records are dynamically updated in real-time whenever a face is successfully detected. This automated synchronization between face detection and database updates ensures a seamless and immediate reflection of attendance changes.

Overall, this solution provides a robust and efficient mechanism for real-time face recognition with instant updates to the connected Firebase database. It facilitates a streamlined and effective attendance management system, enhancing efficiency and reliability in various applications.

![Capture d'écran 2023-12-04 122350](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/5ca28e34-2116-4aa9-a4a3-21281fedb680)
![Capture d'écran 2023-12-04 122428](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/acb8c4ec-c05f-46c6-b073-efdfc9ec8522)

# 4- Face_Emotion_Recognition

The provided code implements a real-time facial emotion detection system using a pre-trained deep learning model and the OpenCV library. The goal of the system is to analyze facial expressions captured by a webcam and classify them into different emotions such as anger, disgust, fear, happiness, neutral, sadness, and surprise.

The code begins by importing the necessary libraries, including OpenCV, Keras, NumPy, CSV, and time. These libraries provide functionalities for computer vision tasks, deep learning model loading, numerical computations, CSV file operations, and time-related operations.

Next, the script loads a pre-trained deep learning model from a JSON file. The model architecture is defined in the JSON file, and the model's weights are loaded from a separate file. This process is done using the model_from_json function from the Keras library.

Additionally, the script loads a pre-trained face cascade classifier from the OpenCV library. This classifier is used to detect faces in the captured webcam frames. The cascade classifier file is loaded from the cv2.data.haarcascades directory.

To extract features from the captured facial images, the code defines a function that converts the image to grayscale, reshapes it to the required format by the model, and normalizes the features. This function is used to preprocess the face regions before feeding them into the model for emotion prediction.

![Capture d'écran 2023-12-04 124707](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/6e3034d6-2b6d-4c17-8bbd-5b7ebb3d5eaf)
![Capture d'écran 2023-12-04 124720](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/54a486fa-4040-420f-aa3c-cf42195577ef)

## Requirements

- PC or Laptop
- Web Cam
- Python 3.7 or higher
- windows or linux
- Visual Studio
- Firebase Account
- Internet

## Future Plan

As part of the future plan, the goal is to enhance the recognition rate of the face recognition system to improve students academic success, specifically when there are unintentional changes in a person's appearance, such as shaving the head, wearing a scarf, or growing a beard. The intention is to improve the system's ability to accurately identify individuals despite these changes.
