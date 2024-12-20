import cv2
def start():
    cam=cv2.VideoCapture(0)
    while True:
        ret,frame=cam.read()
        cv2.imshow("image",frame)
        k = cv2.waitKey(100) & 0xff # Waits for a pressed key
        if k == 27: # Press 'ESC' to stop
            break
    cam.release()
    cv2.destroyAllWindows()