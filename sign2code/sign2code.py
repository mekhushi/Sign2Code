import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

def count_fingers_detailed(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []

    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def get_html_tag_from_fingers(fingers):

    if fingers == [0,1,0,0,0]:
        return "<h1>Heading 1</h1>"
    elif fingers == [0,1,1,0,0]:
        return "<p>Paragraph</p>"
    elif fingers == [0,1,1,1,0]:
        return "<div>Division</div>"
    elif fingers == [0,1,1,1,1]:
        return "<ul><li>List Item</li></ul>"
    elif fingers == [1,1,1,1,1]:
        return '<a href="#">Link</a>'
    elif fingers == [1,0,0,0,0]:
        return "<button>Click Me</button>"
    elif fingers == [0,1,1,0,0]:
        return '<img src="image.jpg" />'
    elif fingers == [0,0,1,0,0]:
        return "<span></span>"
    elif fingers == [0,0,0,1,0]:
        return '<input type="text" />'
    elif fingers == [0,0,0,0,1]:
        return "<form></form>"
    else:
        return ""


cap = cv2.VideoCapture(0)

last_tag = ""
cooldown = 3  # seconds cooldown between typing to avoid spamming
last_time = time.time() - cooldown

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    tag_text = ""
    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        fingers = count_fingers_detailed(hand_landmarks)
        tag_text = get_html_tag_from_fingers(fingers)

        # Agar naye tag mila hai aur cooldown khatam hua hai, tabhi type karo
        if tag_text and tag_text != last_tag and (time.time() - last_time) > cooldown:
            print(f"Typing tag: {tag_text}")
            pyautogui.write(tag_text, interval=0.05)
            pyautogui.press('enter')
            last_tag = tag_text
            last_time = time.time()

    cv2.putText(frame, f"Detected: {tag_text}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Sign to VS Code Typing", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
