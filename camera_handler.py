import cv2

def start_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return cap

def read_frame(cap):
    success, frame = cap.read()
    return success, cv2.flip(frame, 1) if success else (False, None)

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
