import cv2
import cv2.cv as cv
#cascade = cv2.CascadeClassifier("part2.xml")


def detect(image):
 image_faces = []
 bitmap = cv.fromarray(image)
 cascade = cv.Load('C:\\Users\\matbr\\Documents\\Visual Studio 2015\\Projects\\PythonApplication1\\PythonApplication1\\part2.xml')
 print(cascade)
 faces = cv.HaarDetectObjects(bitmap, cascade, cv.CreateMemStorage(0))
 if faces:
  for (x,y,w,h),n in faces:
   image_faces.append(image[y:(y+h), x:(x+w)])
   #cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)
 return image_faces
if __name__ == "__main__":
    while 1:
        img = cv2.imread("part1_decoded")

        image_faces = []
        image_faces = detect(img)
        for i, face in enumerate(image_faces):
           cv2.imwrite("face-" + str(i) + ".jpg", face)

        #cv2.imshow("features", frame)
        if cv2.waitKey(1) == 0x1b: # ESC
            print 'ESC pressed. Exiting ...'
            break

