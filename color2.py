# import the opencv library
import cv2
import numpy as np
import matplotlib.pyplot as plt

## if nothing found, do nothing
def nothing(x):
    #any operation
    pass

# define a video capture object which connects our camera to system
vid = cv2.VideoCapture(0) ## Zero for webcam and 1, 2... for externel devices

"""
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)
"""

while True:

    # Capture the video frame
    # by frame
    _, frame = vid.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # defining red color boundaries
    lower_red = np.array([161, 155, 84], dtype="uint8")
    upper_red = np.array([179, 255, 255], dtype="uint8")
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    #red = cv2.bitwise_and(frame, frame, mask=red_mask)

    #l_h = cv2.getTrackbarPos("L-H", "Trackbars")

    #contours detection
    #_, contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #for cnt in contours:
    #   cv2.drawContours(frame, [cnt], 0, (0, 0, 0))

    cv2.imshow("Frame", frame)
    cv2.imshow("Red Mask", red_mask)
    #frame = cv2.bitwise_and(frame, frame, mask=mask)
    # Display the resulting frame

    ## Exit with ESC(27) loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()