# cv2.VideoWriter(): creates a video writer object that can be used to write frames to a video file.
# The syntax for cv2.VideoWriter() is as follows:
# cv2.VideoWriter(filename, fourcc, fps, frameSize)
# where:
# - filename: the name of the file to which we want to save the video (e.g., "output.mp4").
# - fourcc: the codec to be used for encoding the video 
# #(e.g., cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')).
# - fps: the frames per second for the video.
# - frameSize: the size of each frame in the video (width, height).

import cv2

camera = cv2.VideoCapture(0) # create a video writer object


frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) # get the width of the video frames
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) # get the height 

fourcc = cv2.VideoWriter_fourcc(*'XVID') # define the codec for encoding the video

recorder = cv2.VideoWriter("output.avi", fourcc, 20.0, (frame_width, frame_height)) # create a video writer object

while True:
    ret, frame = camera.read() # read a frame from the video source

    if not ret:
        print("Failed to capture video.")
        break

    recorder.write(frame) # write the captured frame to the video file

    cv2.imshow("Recording Video", frame) # display the captured video frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for the 'q' key to be pressed to exit
        break

camera.release() # release the video capture object
recorder.release() # release the video writer object
cv2.destroyAllWindows() # close the window