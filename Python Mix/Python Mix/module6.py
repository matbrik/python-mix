import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('part2.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is the cascade we just made. Call what you want
#watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')

#cap = cv2.VideoCapture(0)
i=0
while i==0:
    i=1
    #ret, img = cap.read()
    img = cv2.imread("part1_decoded.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, 1.02,50)
    
    # add this
    # image, reject levels level weights.
    #watches = watch_cascade.detectMultiScale(gray, 50, 50)
    
    # add this
    #for (x,y,w,h) in watches:
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    #print(faces)
    for (x,y,w,h) in faces:
       cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,255),2)
       print(faces)
       print("qw")
        
     #   roi_gray = gray[y:y+h, x:x+w]
     #   roi_color = img[y:y+h, x:x+w]
     #   eyes = eye_cascade.detectMultiScale(roi_gray)
    #    for (ex,ey,ew,eh) in eyes:
    #        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
   


    cv2.imshow('img',gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#cap.release()
#cv2.destroyAllWindows()