import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(2)
imgBackground=cv2.imread('images/bg/bg.png')
video_capture.set(3, 640)
video_capture.set(4, 480)

wah_img = face_recognition.load_image_file("images/6116.jpg")
wah_encoding = face_recognition.face_encodings(wah_img)[0]

nam_img = face_recognition.load_image_file("images/6119.jpg")
nam_encoding = face_recognition.face_encodings(nam_img)[0]

ash_img = face_recognition.load_image_file("images/6126.png")
ash_encoding = face_recognition.face_encodings(ash_img)[0]

ksh_img = face_recognition.load_image_file("images/6145.png")
ksh_encoding = face_recognition.face_encodings(ksh_img)[0]

ket_img = face_recognition.load_image_file("images/6150.png")
ket_encoding = face_recognition.face_encodings(ket_img)[0]

kru_img = face_recognition.load_image_file("images/6160.png")
kru_encoding = face_recognition.face_encodings(kru_img)[0]

ajy_img = face_recognition.load_image_file("images/6162.png")
ajy_encoding = face_recognition.face_encodings(ajy_img)[0]
known_face_encoding = [
    wah_encoding,
    nam_encoding,
    ash_encoding,
    ksh_encoding,
    ket_encoding,
    kru_encoding,
    ajy_encoding
    ]
known_face_roll = [
    "6116",
    "6119",
    "6126",
    "6145",
    "6150",
    "6160",
    "6162"
    ]
known_face_names = [
    "WAHID CHOUGLE",
    "NAMAN MATHUR",
    "ASHISH CHANCHLANI",
    "KAASHVI HIRANANDANI",
    "KETAN PATEL",
    "KRUTIKA OJHA",
    "AJEY NAGAR"
    ]
known_face_class = [
    "SYIT",
    "SYIT",
    "SYIT",
    "SYIT",
    "SYIT",
    "SYIT",
    "SYIT"
    ]
known_face_div = [
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A"
    ]

rstudents = known_face_roll.copy()
students = known_face_names.copy()
cstudents = known_face_class.copy()
dstudents = known_face_div.copy()

face_locations = []
face_encodings = []
face_roll = []
face_names = []
face_class = []
face_div = []
s=True

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(current_date+".csv", "w+", newline = "")
lnwriter = csv.writer(f)
lnwriter.writerow(['ROLL NO', 'NAME', 'CLASS', 'DIVISON', 'TIME'])
current_time = now.strftime("%I-%M-%S-%p")
while True:
    success, frame = video_capture.read()
    imgBackground[178:178+480, 328:328+640]= frame
    small_frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            roll=""
            name=""
            clas=""
            div=""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                roll = known_face_roll[best_match_index]
                name = known_face_names[best_match_index]
                clas = known_face_class[best_match_index]
                div = known_face_div[best_match_index]
                cv2.putText(imgBackground, name+" PRESENT!", (340,650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,155,0), 2)
            else:
                cv2.putText(imgBackground, "UNREGISTERED USER!", (340,650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,155), 2)
            face_roll.append(roll)
            face_names.append(name)
            face_class.append(clas)
            face_div.append(div)
             
            if roll in known_face_roll:
                if roll in rstudents:
                    rstudents.remove(roll)
                    print("Absent Students Roll No: ", rstudents)
                    at=len(rstudents[::1])
                    pt=len(face_roll[::1])
                    tt=len(known_face_roll[::1])

                    if name in known_face_names:
                        if name in students:
                            students.remove(name)
                            if clas in known_face_class:
                                if clas in cstudents:
                                    cstudents.remove(clas)
                                    if div in known_face_div:
                                        if div in dstudents:
                                            dstudents.remove(div)
                                            lnwriter.writerow([roll, name, clas, div, current_time])                    
                                        
                
    cv2.imshow("ATTENDANCE SYSTEM", imgBackground)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

lnwriter.writerow(['TOTAL STUDENTS: ', tt])
lnwriter.writerow(['ABSENT STUDENTS: ', at])
lnwriter.writerow(['PRESENT STUDENTS: ', pt])
f.close()
