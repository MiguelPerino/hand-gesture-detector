import cv2
from gesture_detector import GestureDetector
from utils.drawing import draw_landmarks, draw_hand_info
from gestures.hand_gestures import count_fingers, is_peace, is_thumbs_up, is_thumbs_down, is_hang_loose
# Inicializa a webcam (0 representa a câmera padrão do computador)
cap = cv2.VideoCapture(0)

gesture = GestureDetector()

while True:
    # Captura frame por frame
    ret, frame = cap.read() 
    #ret retorna true ou false, pra ver se retornou o frame corretamente
    
    # Se o frame não for lido corretamente, encerra o loop
    if not ret:
        break
    
    # Exibe o frame capturado em uma janela

    results = gesture.process(frame)

    if results.hand_landmarks:
        draw_landmarks(frame, results)
        for i, (hand_landmarks, handedness) in enumerate(zip(results.hand_landmarks, results.handedness)):   #usar enumerate pra detectar qual mão é, assim nao sobrescreve a escrita de count_fingers
            side = handedness[0].category_name
            total = count_fingers(hand_landmarks, side)
            peace = is_peace(hand_landmarks, side)
            thumbs_up = is_thumbs_up(hand_landmarks, side)
            thumbs_down = is_thumbs_down(hand_landmarks, side)
            hang_loose = is_hang_loose(hand_landmarks, side)
            
            draw_hand_info(frame, total, peace, i, side, thumbs_up, thumbs_down, hang_loose)
            
    cv2.imshow('Video - Webcam', frame)

    # Aguarda 1 milissegundo; se a tecla 'q' for pressionada, sai do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o recurso da webcam e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
