# Indicador 8  6
# Médio12 10
# Anelar 16   14
# Mindinho 20 18
#dedao 4 2


def count_fingers(hand_landmarks, side):
    fingers_y = [8, 12, 16, 20]
    middle_y = [5, 9, 13, 17]

    up = []
    for  tip, joint in zip(fingers_y, middle_y):
        if hand_landmarks[tip].y < hand_landmarks[joint].y:
            up.append(1)
        
    if side == "Right":
        if hand_landmarks[4].x > hand_landmarks[2].x:
            up.append(1)
        
    else:
        if hand_landmarks[4].x < hand_landmarks[2].x:
            up.append(1)

    return len(up)

def is_up(landmarks, side):
    fingers_y = [8, 12, 16, 20]
    middle_y = [5, 9, 13, 17]

    up = []
    if side == "Right":
        if landmarks[4].x > landmarks[2].x:
            up.append(True)
        else:
            up.append(False)     
               
    else:
        if landmarks[4].x < landmarks[2].x:
            up.append(True)
        else:
            up.append(False)
            
    for  tip, joint in zip(fingers_y, middle_y):
        if landmarks[tip].y < landmarks[joint].y:
            up.append(True)
        else:
            up.append(False)
                    
    return up


def is_peace(landmarks, side):
    # is_up lista boolean [Polegar, indicador, médio, anelar, mindinho]
    up = is_up(landmarks, side)
    
    return up[1] and up[2] and not up[3] and not up[4] and not up[0]
    