from flask import Flask, render_template, Response
import cv2
from gesture_detector import GestureDetector
from utils.drawing import draw_landmarks, draw_hand_info
from gestures.hand_gestures import count_fingers, is_peace, is_thumbs_down, is_thumbs_up, is_hang_loose


app = Flask(__name__)
cap = cv2.VideoCapture(0)
gesture = GestureDetector()

def generate_frames():
    while True:
        ret, frame = cap.read()
        
        # Se o frame não for lido corretamente, encerra o loop
        if not ret:
            break
        
        results = gesture.process(frame)
        
        if results.hand_landmarks:
            draw_landmarks(frame, results)
            for i, (hand_landmarks, handedness) in enumerate(zip(results.hand_landmarks, results.handedness)):
                side = handedness[0].category_name
                total = count_fingers(hand_landmarks, side)
                
                peace = is_peace(hand_landmarks, side)
                
                thumbs_up = is_thumbs_up(hand_landmarks, side)

                thumbs_down = is_thumbs_down(hand_landmarks, side)
                
                hang_loose = is_hang_loose(hand_landmarks, side)
            
                draw_hand_info(frame, total, peace, i, side, thumbs_up, thumbs_down, hang_loose)
            
        ret, buffer = cv2.imencode('.jpg', frame)
        
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)



