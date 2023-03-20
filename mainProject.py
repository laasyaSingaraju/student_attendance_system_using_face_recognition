# STUDENT ATTENDANCE MANAGEMENT SYSTEM
import face_recognition
import cv2
import pygame
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import sys
import datetime
#Module 1:Data Load Module
fnt = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 30) #selecting font
f = pd.read_csv('./venv/student.csv')

rollno = f["RollNo"].tolist()
name = f["Name"].tolist()
clg = f["College"].tolist()
branch = f["Branch"].tolist()
picname = f["PhotoLocation"].tolist()
#audioname = f["AudioLocation"].tolist()
student = []
student_encode = []
#audio = []

n = len(rollno)
for i in range(n):
    student .append(face_recognition.load_image_file(picname[i]))
    student_encode.append(face_recognition.face_encodings(student[i])[0])
#print("HI")
#Module 2:Face Capture Module
camera = cv2.VideoCapture(0)
for i in range(9):
    return_value, image = camera.read()
    #print(return_value, image.shape)
    cv2.imwrite('photo'+str(i)+'.png', image)
del(camera)
unknown = face_recognition.load_image_file("photo5.png")
#Module 3 : Face Recognition Module
def recognize_student(image):
    try:
        unknown_encode = face_recognition.face_encodings(image)[0]
    except IndexError as e:
        print(e)
        sys.exit(1)

    match=face_recognition.compare_faces(student_encode,unknown_encode,tolerance=0.5)
    #print(match)
    index=-1
    for i in range(n):

       if match[i]:
           index=i
    return index
#Module 4: Record Attendance Module
studentIndex = recognize_student(unknown)
print(studentIndex)
if(studentIndex!=-1):
    x = str(datetime.datetime.now())
    attend = "\n" + str(rollno[studentIndex]) + " " + str(name[studentIndex] + " " +clg[studentIndex] + " "+branch[studentIndex] +" " +x)
    print(attend)
    f = open("./venv/attendance.txt", "a")
    f.write(attend)
    f.close
#Module 5:Display Face Module
#pil_image=Image.fromarray(student[studentIndex])
#pil_image=Image.fromarray(unknown)
#draw=ImageDraw.Draw(pil_image)
if(studentIndex!=-1):
    Name = name[studentIndex]+"Face is recognized"
    pil_image = Image.fromarray(student[studentIndex])
    draw = ImageDraw.Draw(pil_image)
    x = 100
    y = student[studentIndex].shape[0] - 100
else:
    Name = "Face is not recognized"
    pil_image=Image.fromarray(unknown)
    draw = ImageDraw.Draw(pil_image)
    x=100
    y=unknown.shape[0]-100
#y=student[studentIndex].shape[0]-100
#y=unknown.shape[0]-100
draw.text((x,y),Name,font=fnt,fill=(0,255,0))
pil_image.show()

'''# Module 6 Announce Attendance Recorded Module
audioloc = audio[studentIndex]
pygame.mixer.init()
if emp_index ==-1:
    pygame.mixer.music.load(
        "./venv/audio/lasya.mp3")
    pygame.mixer.music.play()
else:
    pygame.mixer.music.load(audioloc)
    pygame.mixer.music.play()
    pygame.mixer.music.queue(
        "./venv/audio/successfully.mp3")
    pygame.mixer.music.play()'''
