# 🌟 Gesture-Based LED Brightness Control (Computer Vision + Arduino)

This project demonstrates a touchless physical computing interface where the brightness of an LED is controlled using hand gestures. Using MediaPipe and OpenCV, the system measures the distance between the user's thumb and index finger and sends a real-time brightness value (0–255) to an Arduino, which drives an LED using PWM.

This project highlights how computer vision can interact with physical hardware, enabling smart interfaces and assistive technologies.

# 🚀 Features

Real-time hand tracking using MediaPipe

Detects distance between finger landmarks

Converts distance → PWM brightness value

Sends data to Arduino via serial communication

Smooth, touch-free LED dimming

Supports external webcams

Lightweight and easy to run

# 🧩 How It Works


Camera → OpenCV → MediaPipe Hand Tracking → Distance Calculation → Serial → Arduino → PWM → LED


Camera captures hand in real time

MediaPipe detects 21 hand landmarks

Distance between thumb tip & index finger tip is measured

Distance is mapped to a brightness level (0–255)

Value is sent to Arduino over USB serial

Arduino sets LED brightness using analogWrite()

# 🛠️ Hardware Requirements

Arduino Uno / Nano / Mega

LED

220Ω resistor

Breadboard

Jumper wires

Webcam (inbuilt or external)

USB cable

🔌 Simple Circuit
Arduino Pin 9 → LED (+)
LED (–) → 220Ω resistor → GND

# 💻 Software Requirements

Python 3.10 (MediaPipe does not support 3.12+)

Arduino IDE

Python libraries:

mediapipe

opencv-python

pyserial

# Use external camera if needed → change index to 1, 2, etc.
cap = cv2.VideoCapture(1)

🔍 Selecting the Correct Camera

Use this helper script:

import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)
    print(f"Camera {i} available:", cap.isOpened())
    cap.release()


Update:

cap = cv2.VideoCapture(<index>)

🧪 Testing the Serial Port

Check available COM ports:

python -m serial.tools.list_ports


Update in Python:

arduino = serial.Serial('COM4', 9600)

# 🎯 Applications

Touchless smart home control

Assistive interfaces

Gesture-based IoT

Interactive art installations

Human–computer interaction demos

# 📄 License

This project is licensed under the MIT License.

# 💬 Contribute

Contributions, improvements, and suggestions are welcome.
You can help expand this into a multi-gesture or multi-device control system.

Install using:

pip install -r requirements.txt

