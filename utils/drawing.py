import cv2

def draw_landmarks(frame, results):
    
    for hand_landmarks in results.hand_landmarks:
        
        for landmarks in hand_landmarks:

            h, w, _ = frame.shape
            x = int(landmarks.x * w)
            y = int(landmarks.y * h)

            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)


def draw_fingers_count(frame, total, hand_index):
    y_position = 50 + (hand_index * 50) #se for index 1 (mao 1) fica 50 px, se for mao 2 (index 2) fica 100px
    cv2.putText(frame, f'Dedos: {total}', (10, y_position),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


