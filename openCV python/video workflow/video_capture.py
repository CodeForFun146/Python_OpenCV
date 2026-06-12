#cv2.videocapture(): captures video from a specified source 
# #(e.g., webcam, video file).
#- source: the video source (e.g., 0 for the default webcam, 
# # or a file path for a video file).
#- returns: a VideoCapture object that can be used 
# # to read frames from the video source

import cv2

cap = cv2.VideoCapture(0) # capture video from the default webcam (source 0)

while True:
    ret, frame = cap.read() # read a frame from the video source

    if not ret:
        print("Failed to capture video.")
        break   

    cv2.imshow("Webcam Video", frame) # display the captured video frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for the 'q' key to be pressed to exit
        break

cap.release() # release the video capture object
cv2.destroyAllWindows() # close the window
