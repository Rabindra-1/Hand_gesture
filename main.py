import cv2
import mediapipe as mp
import pyautogui
import math
import time





mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

screen_w , screen_h = pyautogui.size()
prev_screen_x,prev_screen_y = 0,0

hands = mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)


cap = cv2.VideoCapture(0)

click_start_time = 0
click_times=[]
click_cooldown = 0.5
scroll_mode = False
freeze_cursor = False
screenshot_cooldown = 2
last_screenshot_time = 0


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
            1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y else 0
            for tip in [8, 12, 16, 20]
        ]

        distance = math.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)
        if distance <0.06:
            if not freeze_cursor:
                freeze_cursor = True
                click_times.append(time.time())

                if len(click_times) >= 2 and click_times[-1] - click_times[-2] < 0.4:
                    pyautogui.doubleClick()
                    cv2.putText(frame, 'Double Click', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    click_times = []
                else:
                    pyautogui.click()
                    cv2.putText(frame, 'Click', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        else:
            freeze_cursor = False

        #for index finger movement
        if not freeze_cursor:
            screen_x = int(index_tip.x * screen_w)
            screen_y = int(index_tip.y * screen_h)
            pyautogui.moveTo(screen_x, screen_y, duration=0.05)
            prev_screen_x, prev_screen_y = screen_x, screen_y

            curr_screen_x = prev_screen_x + (screen_x - prev_screen_x) / 5
            curr_screen_y = prev_screen_y + (screen_y - prev_screen_y) / 5

            pyautogui.moveTo(curr_screen_x, curr_screen_y)
            prev_screen_x, prev_screen_y = curr_screen_x, curr_screen_y



        # Screen shot
        if sum(fingers) == 0:
            current_time = time.time()
            if current_time - last_screenshot_time > screenshot_cooldown:
                pyautogui.screenshot('screenshot.png')
                cv2.putText(frame, 'Screenshot Taken', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                last_screenshot_time = current_time




    cv2.imshow('frame',frame)
    if cv2.waitKey(1) ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
