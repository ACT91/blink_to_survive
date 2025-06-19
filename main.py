import cv2
from camera_handler import start_camera, read_frame, release_camera
from blink_detector import get_landmarks, is_blinking
from key_controller import send_space_if_not_on_cooldown

def main():
    cap = start_camera()

    while cap.isOpened():
        success, frame = read_frame(cap)
        if not success:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        landmarks_list = get_landmarks(image_rgb)

        if landmarks_list:
            for landmarks in landmarks_list:
                if is_blinking(landmarks.landmark):
                    send_space_if_not_on_cooldown()

        cv2.imshow("Blink to Survive", frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    release_camera(cap)

if __name__ == "__main__": 
    main()
