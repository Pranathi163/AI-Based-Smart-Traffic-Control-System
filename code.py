pip install opencv-python numpy

import cv2
import time

# Load the pre-trained Haar cascade classifier for car detection
car_cascade = cv2.CascadeClassifier('cars.xml')

# Start video capture (0 for webcam or provide video file path)
cap = cv2.VideoCapture(0)  # Replace with 'video.mp4' if using video

def detect_vehicles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    return cars

def simulate_traffic_light(vehicle_count):
    if vehicle_count > 20:
        green_time = 30
    elif vehicle_count > 10:
        green_time = 20
    elif vehicle_count > 5:
        green_time = 15
    else:
        green_time = 10

    print(f"[GREEN] signal ON for {green_time} seconds (Vehicles: {vehicle_count})")
    time.sleep(green_time)
    print("[RED] signal ON for 5 seconds")
    time.sleep(5)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to get frame from camera. Exiting...")
        break

    cars = detect_vehicles(frame)
    vehicle_count = len(cars)

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display frame with detections
    cv2.putText(frame, f'Vehicle Count: {vehicle_count}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('AI Smart Traffic System', frame)

    simulate_traffic_light(vehicle_count)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
