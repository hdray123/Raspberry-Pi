#coding:utf-8
import cv2
cap= cv2.VideoCapture(0)
cv2.namedWindow('main')
while(cap.isOpened()):
    ret,img=cap.read()
    #开关输入信号：如果flase表示不拍照，true表示拍照
    take_photo_single=False
    if ret :
        cv2.imshow('main', img)
        k = cv2.waitKey(1) & 0xff
        if k==ord('q') or take_photo_single:
            cv2.imwrite('cc.jpg',img)
            break;
cap.release()

cv2.destroyAllWindows()
