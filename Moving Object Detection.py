import cv2
import imutils

first_frame = None
Area = 500

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    text = 'Nomal'
    img = imutils.resize(img,width = 500)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_img = cv2.GaussianBlur(gray_img,(21,21),0)

    if first_frame is None:
        first_frame = gray_img
        continue
    imgDiff = cv2.absdiff(first_frame,gray_img)
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg,None,iterations = 2)
    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c)>Area:
            continue
        (x,y,h,w) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text = 'Moving Objected detected'
        print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow('VideoStream',img)
    
    if cv2.waitKey(1) == ord('q') & 0xFF:
        break
cam.release()
cv2.destroyALLWindows()

    
