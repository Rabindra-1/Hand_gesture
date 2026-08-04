import cv2
import mediapipe as mp
import pyautogui



mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

screen_w , screen_h = pyautogui.size()
prev_screen_x = 0, prev_screen_y = 0

hands = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame")
        exit()
    frame=cv2.flip(frame,1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

        thumb_tip=hand_landmarks.landmark[4]
        index_tip=hand_landmarks.landmark[8]
        middle_tip=hand_landmarks.landmark[12]
        ring_tip=hand_landmarks.landmark[16]
        pinkey_tip=hand_landmarks.landmark[20]

        fingers = [
            1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y else 0,
        ]

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
