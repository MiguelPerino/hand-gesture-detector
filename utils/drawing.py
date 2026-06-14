import cv2

def draw_landmarks(frame, results):
    
    for hand_landmarks in results.hand_landmarks:
        
        h, w, _ = frame.shape
        for landmarks in hand_landmarks:
            x = int(landmarks.x * w)
            y = int(landmarks.y * h)

            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)


BLOCK_SIZE = 120
def draw_hand_info(frame, total, peace, hand_index, side, thumbs, thumbs_down):
    y_position = 50 + (hand_index * BLOCK_SIZE)
    
    cv2.putText(frame, f'Mao: {side}', (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 0), 2)
    cv2.putText(frame, f"Fingers UP Right: {total}", (10, y_position + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255, 0), 2)
    
    if peace:
        cv2.putText(frame, f"PAZ E AMOR RAPAZ Right: {peace}", (10, y_position + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if thumbs:
        cv2.putText(frame, f"JOINHA PRO CE: {thumbs}", (10, y_position + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if thumbs_down:
        cv2.putText(frame, f"Negativo: {thumbs_down}", (10, y_position + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)