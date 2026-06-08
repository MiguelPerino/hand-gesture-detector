import cv2
from gesture_detector import GestureDetector
from utils.drawing import draw_landmarks, draw_fingers_count
from gestures.hand_gestures import count_fingers
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
        for i, hand_landmarks in enumerate(results.hand_landmarks):   #usar enumerate pra detectar qual mão é, assim nao sobrescreve a escrita de count_fingers
            total = count_fingers(hand_landmarks)
            draw_fingers_count(frame, total, i)
            print(f'{total} dedos levantados')

    cv2.imshow('Video - Webcam', frame)

    # Aguarda 1 milissegundo; se a tecla 'q' for pressionada, sai do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera o recurso da webcam e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()
