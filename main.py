import cv2

MaskaCascade = cv2.CascadeClassifier("resursi/maskCascadeV6.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, img1 = cap.read()
    img1Gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

    mask = MaskaCascade.detectMultiScale(img1Gray,1.1,4)
    for (x,y,w,h) in mask:
        cv2.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Mask", img1)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.realease()
cv2.destroyAllWindows()
