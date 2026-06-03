import cv2

def draw_landmarks(frame, results):
    
    for hand_landmarks in results.hand_landmarks:
        
        for landmarks in hand_landmarks:

            h, w, _ = frame.shape
            x = int(landmarks.x * w)
            y = int(landmarks.y * h)

            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)


