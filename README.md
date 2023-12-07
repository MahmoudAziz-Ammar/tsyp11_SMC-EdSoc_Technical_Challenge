## Analysis Part

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



# Face Recognition with Real Time

## Description

This project leverages Python and OpenCV to implement real-time face recognition capabilities. It utilizes Python 3.7, higherOpenCV, cvzone, numpy, face_recognition, and the Firebase Admin SDK to achieve accurate and efficient face recognition in various real-time scenarios.

## Requirements

- PC or Laptop
- Web Cam
- Python 3.7 or higher
- windows or linux
- Visual Studio
- Firebase Account
- Internet

## Sample Output
![Capture d'écran 2023-12-04 115114](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/6da22082-41c6-4778-9fc4-ae1cebc7e354)
![Capture d'écran 2023-12-04 124707](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/6e3034d6-2b6d-4c17-8bbd-5b7ebb3d5eaf)
![Capture d'écran 2023-12-04 124720](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/54a486fa-4040-420f-aa3c-cf42195577ef)


## Real Time Database

The development of a real-time face recognition system requires the integration of advanced facial recognition algorithms with a live camera feed. To achieve this, a seamless connection to a Firebase real-time database is established. This enables the system to upload scanned faces dynamically, ensuring efficient storage in the database while simultaneously updating attendance records. As individuals are recognized in real-time, their corresponding photos are securely stored in Firebase storage, providing a comprehensive solution for accurate attendance tracking.

The implementation of real-time face recognition involves the integration of a system that seamlessly connects to a live database, such as Firebase. When faces are scanned in real-time, the captured images are instantly uploaded to the Firebase database, ensuring a swift and efficient storage process. At the same time, the attendance records are dynamically updated in real-time whenever a face is successfully detected. This automated synchronization between face detection and database updates ensures a seamless and immediate reflection of attendance changes.

Overall, this solution provides a robust and efficient mechanism for real-time face recognition with instant updates to the connected Firebase database. It facilitates a streamlined and effective attendance management system, enhancing efficiency and reliability in various applications.

![Capture d'écran 2023-12-04 122350](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/5ca28e34-2116-4aa9-a4a3-21281fedb680)
![Capture d'écran 2023-12-04 122428](https://github.com/bilel910/tsyp11_SMC-EdSoc_Technical_Challenge/assets/83314544/acb8c4ec-c05f-46c6-b073-efdfc9ec8522)

### Requirements

- Python 3.3+ or Python 2.7
- macOS or Linux or Windows 

`brew install cmake`

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

## Future Plan

As part of the future plan, the goal is to enhance the recognition rate of the face recognition system to improve students academic success, specifically when there are unintentional changes in a person's appearance, such as shaving the head, wearing a scarf, or growing a beard. The intention is to improve the system's ability to accurately identify individuals despite these changes.
