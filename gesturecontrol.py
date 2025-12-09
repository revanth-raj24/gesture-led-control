import cv2
import mediapipe as mp
import serial
import time
import math

# Connect to Arduino
arduino = serial.Serial('COM8', 9600)   # Change COM port if needed
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

min_dist = 20     # minimum finger distance
max_dist = 200    # maximum finger distance

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Thumb tip = 4, Index tip = 8
            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]

            h, w, _ = img.shape
            x1, y1 = int(thumb.x * w), int(thumb.y * h)
            x2, y2 = int(index.x * w), int(index.y * h)

            # Distance between thumb & index
            dist = math.hypot(x2 - x1, y2 - y1)

            # Map distance to PWM (0 - 255)
            brightness = int((dist - min_dist) / (max_dist - min_dist) * 255)
            brightness = max(0, min(255, brightness))

            # Send PWM value to Arduino
            arduino.write(f"{brightness}\n".encode())

            # Display
            cv2.putText(img, f'Brightness: {brightness}', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.circle(img, (x1, y1), 8, (255, 0, 0), -1)
            cv2.circle(img, (x2, y2), 8, (255, 0, 0), -1)

    cv2.imshow("Gesture LED Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
