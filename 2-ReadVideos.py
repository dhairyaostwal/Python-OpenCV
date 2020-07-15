from cv2 import cv2

cap = cv2.VideoCapture(0)

# capturing frame continuously and indefinitely

while(True):
    ret, frame = cap.read()

    # ret would contain true or false
    # frame would capture or contain the frame

    cv2.imshow('Frame-Test', frame) #showing the frame inside window

    # below code if I press 'q' it'll quit the window
    # code works well in terminal not in VSCode Terminal

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()