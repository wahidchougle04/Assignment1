# Automated Face-Recognition Attendance System

An automated computer vision solution built in Python that logs real-time attendance using face recognition, overlays live status on a custom graphical user interface (GUI), and exports comprehensive daily attendance reports to CSV format.

---

## Project Overview

Manual attendance tracking in academic and professional environments is time-consuming and prone to human error. This system automates attendance by capturing live video feed via webcam, extracting 128-d face embeddings, and matching them against a database of registered student profiles using Euclidean distance. 

Upon identification, the system marks the student as **Present**, timestamps the record, logs their details into a dynamic daily CSV file, and calculates class summary metrics (Total, Present, and Absent counts).

---

## Tech Stack & Dependencies

* **Language:** Python 3.x
* **Computer Vision:** `opencv-python` (OpenCV)
* **Face Recognition Engine:** `face_recognition` (built on `dlib`)
* **Data Processing & Handling:** `numpy`, `csv`, `datetime`, `os`

---

## Key Features

* **Real-Time Detection & Recognition:** Resizes live video frames for faster frame processing and extracts facial features to match known embeddings.
* **Custom UI Background Overlay:** Integrates the webcam feed directly onto a custom graphical interface (`bg.png`) with live visual status indicators (`PRESENT!` or `UNREGISTERED USER!`).
* **Automated Daily File Generation:** Dynamically creates CSV log files named after the current date (`DD-MM-YYYY.csv`).
* **Duplicate Prevention:** Ensures that once a student is logged, subsequent frames do not duplicate their entry in the daily attendance sheet.
* **Summary Analytics:** Appends total class strength, total present count, and total absent count at the end of the CSV report upon exiting.

---

## System Workflow

```text
  [ Webcam Capture ] ──> [ Frame Downscaling (0.5x) ]
                                    │
                                    ▼
                       [ RGB Conversion & Face Detection ]
                                    │
                                    ▼
                       [ Face Embedding Extraction ]
                                    │
                                    ▼
                    [ Match Against Known Embeddings (Euclidean Distance) ]
                                    │
                  ┌─────────────────┴─────────────────┐
                  ▼                                   ▼
          [ Match Found ]                    [ Unregistered User ]
                  │                                   │
      - Overlay Name & Status             - Display "UNREGISTERED USER!"
      - Log (Roll, Name, Class, Div, Time)
      - Calculate Absent Count

```
## Images Authenticated
<img width="1080" height="1080" alt="face_recog_ajey" src="https://github.com/user-attachments/assets/95a25607-d4b7-4511-825f-e0446fd2c491" />
<img width="1080" height="1080" alt="face_recog_ashish" src="https://github.com/user-attachments/assets/431390be-bef1-41fc-b619-aeda7de32e56" />
<img width="1080" height="1080" alt="face_recog_kaashvi" src="https://github.com/user-attachments/assets/52548e72-cccb-406a-bba5-2d45b9e44f0f" />
<img width="1080" height="1080" alt="face_recog_naman" src="https://github.com/user-attachments/assets/269e0dec-3dee-40c6-b559-5722e6d4a652" />

## Images Unauthenticated
<img width="1080" height="1080" alt="face_recog_hania" src="https://github.com/user-attachments/assets/1732d16d-0b0a-4421-8019-e30fb60fe014" />

## Excel Sheet
<img width="1080" height="1080" alt="face_recog_excelsheet" src="https://github.com/user-attachments/assets/d8b452f4-7699-462e-bbe4-c753a602780a" />
