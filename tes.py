import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import serial
import serial.tools.list_ports
import urllib.request
import os
import time

# === AUTO DOWNLOAD MODEL ===
MODEL_PATH = 'hand_landmarker.task'
MODEL_URL = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task'

if not os.path.exists(MODEL_PATH):
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# === AUTO DETECT ARDUINO ===
def find_arduino_port():
    for p in serial.tools.list_ports.comports():
        desc = p.description.lower()
        hwid = p.hwid.lower()
        if any(keyword in desc or keyword in hwid for keyword in [
            "arduino", "ch340", "ch341", "usb serial", "usb-serial",
            "atmega", "ftdi", "cp210", "usbserial"
        ]):
            return p.device
    return None

port = find_arduino_port()

if port is None:
    manual = input("COM Port (contoh: COM3), Enter untuk skip: ").strip()
    port = manual if manual else None

arduino = None
if port:
    try:
        arduino = serial.Serial(port, 9600, timeout=1)
        time.sleep(2)
    except:
        arduino = None

# === MEDIAPIPE ===
options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=MODEL_PATH),
    num_hands=2,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)

landmarker = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),
    (0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20),
    (5,9),(9,13),(13,17)
]

def draw_landmarks(frame, hand_landmark_list):
    h, w = frame.shape[:2]
    for start_idx, end_idx in HAND_CONNECTIONS:
        start = hand_landmark_list[start_idx]
        end   = hand_landmark_list[end_idx]
        x1, y1 = int(start.x * w), int(start.y * h)
        x2, y2 = int(end.x * w), int(end.y * h)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    for lm in hand_landmark_list:
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

def is_fist(hand_landmark_list):
    tips_ids = [8, 12, 16, 20]
    folded = sum(
        1 for tip_id in tips_ids
        if hand_landmark_list[tip_id].y > hand_landmark_list[tip_id - 2].y
    )
    return folded == 4

def draw_ticker(frame, text, x_offset):
    h, w = frame.shape[:2]
    ticker_h = 50
    ticker_y = h - ticker_h

    cv2.rectangle(frame, (0, ticker_y), (w, h), (0, 0, 180), -1)
    cv2.line(frame, (0, ticker_y), (w, ticker_y), (0, 0, 255), 3)

    font       = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.95
    thickness  = 2

    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_y = ticker_y + (ticker_h + text_h) // 2 - 4

    cv2.putText(frame, text, (x_offset, text_y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    if x_offset + text_w < w:
        cv2.putText(frame, text, (x_offset + text_w + 80, text_y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    return text_w

# === MAIN LOOP ===
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

cv2.namedWindow("Hand Tracking", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Hand Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

last_state   = None
ticker_text  = "...  PAMERAN SMKN 2 MANOKWARI  ...  TEKNIK ELEKTRONIKA  ... KEPALKAN TANGAN UNTUK MENYALAKAN LAMPU ...   "
ticker_x     = None
ticker_speed = 3

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w  = frame.shape[:2]

    if ticker_x is None:
        ticker_x = w

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    results  = landmarker.detect(mp_image)

    # === LOCK STATE: hanya update kalau tangan terdeteksi ===
    if results.hand_landmarks:
        fist_detected = False

        for hand_landmark_list in results.hand_landmarks:
            draw_landmarks(frame, hand_landmark_list)
            if is_fist(hand_landmark_list):
                fist_detected = True

        current_state = '1' if fist_detected else '0'
        if current_state != last_state:
            if arduino:
                arduino.write(current_state.encode())
            last_state = current_state

    # Kalau tidak ada tangan -> state tidak berubah

    # === DRAW TICKER ===
    text_w = draw_ticker(frame, ticker_text, ticker_x)

    ticker_x -= ticker_speed

    if ticker_x + text_w + 80 < 0:
        ticker_x = w

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.write(b'0')
    arduino.close()