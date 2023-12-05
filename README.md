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

## GIF Out Sample

## Real Time Database

The development of a real-time face recognition system requires the integration of advanced facial recognition algorithms with a live camera feed. To achieve this, a seamless connection to a Firebase real-time database is established. This enables the system to upload scanned faces dynamically, ensuring efficient storage in the database while simultaneously updating attendance records. As individuals are recognized in real-time, their corresponding photos are securely stored in Firebase storage, providing a comprehensive solution for accurate attendance tracking.

The implementation of real-time face recognition involves the integration of a system that seamlessly connects to a live database, such as Firebase. When faces are scanned in real-time, the captured images are instantly uploaded to the Firebase database, ensuring a swift and efficient storage process. At the same time, the attendance records are dynamically updated in real-time whenever a face is successfully detected. This automated synchronization between face detection and database updates ensures a seamless and immediate reflection of attendance changes.

Overall, this solution provides a robust and efficient mechanism for real-time face recognition with instant updates to the connected Firebase database. It facilitates a streamlined and effective attendance management system, enhancing efficiency and reliability in various applications.

### Requirements

- Python 3.3+ or Python 2.7
- macOS or Linux (Windows not officially supported, but might work)

`brew install cmake`

Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

```bash
pip3 install face_recognition
```

## Future Plan

As part of the future plan, the goal is to enhance the recognition rate of the face recognition system, specifically when there are unintentional changes in a person's appearance, such as shaving the head, wearing a scarf, or growing a beard. The intention is to improve the system's ability to accurately identify individuals despite these changes.
