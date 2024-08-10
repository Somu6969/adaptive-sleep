import cv2
import time
import os
#import keyboard

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face():
    video_capture = cv2.VideoCapture(0)  # Use the default webcam (change if needed)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # Face detected, user is present
            print("User is present.")
            time.sleep(10)  # Wait for 5 seconds before checking again
        else:
            # No face detected, user is absent
            print("User is absent. Initiating sleep process.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")# Put PC to sleep

  
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_face()
