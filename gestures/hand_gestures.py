# Indicador 8  6
# Médio12 10
# Anelar 16   14
# Mindinho 20 18

def count_fingers(hand_landmarks):
    fingers_y = [8, 12, 16, 20]
    middle_y = [6, 10, 14, 18]

    up = []
    for  tip, joint in zip(fingers_y, middle_y):
        if hand_landmarks[tip].y < hand_landmarks[joint].y:
            up.append(1)
    
    return len(up)
            