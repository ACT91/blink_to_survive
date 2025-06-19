import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Eye landmark indices for EAR (left eye top and bottom)
TOP_LID = 159
BOTTOM_LID = 145

def get_landmarks(image_rgb):
    results = face_mesh.process(image_rgb)
    return results.multi_face_landmarks

def calculate_ear(landmarks):
    top = landmarks[TOP_LID]
    bottom = landmarks[BOTTOM_LID]
    return abs(top.y - bottom.y)               
   
def is_blinking(landmarks, threshold=0.01):
    ear = calculate_ear(landmarks)
    return ear < threshold
     