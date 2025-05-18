import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Initialize
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

screen_w, screen_h = pyautogui.size()
prev_x, prev_y = 0, 0
smooth_factor = 5
click_threshold = 0.03
prev_click_time = 0
prev_middle_y = 0
scroll_threshold = 0.01

while True:
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_image)
    h, w, _ = image.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmarks.landmark[8] 
            x = int(lm.x * screen_w)
            y = int(lm.y * screen_h)

            x = prev_x + (x - prev_x) / smooth_factor
            y = prev_y + (y - prev_y) / smooth_factor

            pyautogui.moveTo(x, y)
            prev_x, prev_y = x, y

            index = hand_landmarks.landmark[8]
            thumb = hand_landmarks.landmark[4]
            distance = math.hypot(index.x - thumb.x, index.y - thumb.y)
            current_time = time.time()

            if distance < click_threshold and current_time - prev_click_time > 0.5:
                pyautogui.click()
                prev_click_time = current_time

            index_y = hand_landmarks.landmark[8].y
            middle_y = hand_landmarks.landmark[12].y
            if abs(index_y - middle_y) < 0.05:
                delta_y = middle_y - prev_middle_y
                if abs(delta_y) > scroll_threshold:
                    pyautogui.scroll(-100 if delta_y > 0 else 100)
                prev_middle_y = middle_y

    cv2.imshow("Hand Gesture Control", image)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
