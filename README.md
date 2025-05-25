# 🤟 Sign2Code ✨

## 📌 Problem Statement

Manually typing repetitive HTML tags while coding can become tedious, especially when you want to maintain a smooth flow of creativity or code on the move. Traditional input devices like keyboard and mouse limit interaction to physical presses, which may not always be the most intuitive or fast method.

**What if you could control your code editor by simply showing hand gestures?**

This project harnesses the power of **real-time hand gesture recognition** using MediaPipe and OpenCV to detect finger positions and convert them into predefined HTML tags typed automatically into your active editor window. This not only speeds up your coding but also brings an innovative, natural way to interact with your development environment. 

---

### 🤚 How It Works

1. **Hand Detection:** Uses MediaPipe's Hand Landmark model to detect a single hand and track finger positions in real-time.
2. **Finger Counting Logic:** Based on the relative positions of finger tip landmarks, the system determines which fingers are raised.
3. **Mapping Gestures to Tags:** Specific finger patterns correspond to HTML tags (like `<h1>`, `<p>`, `<div>`, etc.).
4. **Typing Automation:** Using `pyautogui`, the recognized tag is typed automatically in the focused window (e.g., VS Code).
5. **Cooldown Timer:** Prevents spamming by limiting typing frequency.

---

## ✋ Finger Gestures & Corresponding HTML Tags

| Finger Pattern (Thumb → Pinky) | Hand Gesture Emoji       | HTML Tag                      | Description                            |
| ------------------------------ | ------------------------ | -----------------------------|-------------------------------------|
| `[0, 1, 0, 0, 0]`              | ☝️ (Index finger up)      | `<h1>Heading 1</h1>`          | Single index finger raised           |
| `[0, 1, 1, 0, 0]`              | ✌️ (Peace sign)           | `<p>Paragraph</p>`            | Index + middle fingers raised        |
| `[0, 1, 1, 1, 0]`              | 🤟 (Rock sign)             | `<div>Division</div>`         | Index + middle + ring fingers raised |
| `[0, 1, 1, 1, 1]`              | 🖐️ (Open hand)             | `<ul><li>List Item</li></ul>` | All fingers except thumb raised      |
| `[1, 1, 1, 1, 1]`              | ✋ (All fingers up)         | `<a href="#">Link</a>`        | Full hand raised                     |
| `[1, 0, 0, 0, 0]`              | 👍 (Thumbs up)             | `<button>Click Me</button>`   | Thumb only                          |
| `[0, 0, 1, 0, 0]`              | 🤘 (Sign of the horns)     | `<img src="image.jpg" />`     | Middle finger only                  |
| `[0, 0, 0, 1, 0]`              | 🤚 (Raised hand)           | `<span></span>`               | Ring finger only                   |
| `[0, 0, 0, 0, 1]`              | 🤙 (Call me hand)          | `<input type="text" />`       | Pinky only                        |

---

## 🚀Features

- 🖐️ **Real-time hand detection:** Uses MediaPipe’s state-of-the-art hand landmark detection.
- 🔢 **Accurate finger counting:** Custom logic to detect which fingers are raised.
- ⌨️ **Automated typing:** Types HTML tags into any active text field using PyAutoGUI.
- ⏳ **Spam prevention:** Cooldown mechanism to prevent repeated typing of the same tag.
- 🎥 **Live webcam feed:** Shows hand landmarks and feedback on detected tags.
- 💡 **Extensible:** Easily add new gestures and tags.

---

## 🎯 Use Cases

- 🔥 Speed up web development by quickly inserting HTML boilerplate.
- ✨ Make coding accessible for people with mobility restrictions.
- 🎮 Interactive coding demos and workshops.
- 🖥️ Hands-free control for presentations or live coding sessions.

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.6+
- Webcam connected to your computer

### Installation Steps

1. Clone the repo:

 ```bash
   git clone https://github.com/mekhushi/Sign2Code.git
   cd Sign2Code
```

### Install dependencies:
```bash
 pip install opencv-python mediapipe pyautogui
```

----

### ▶️ How to Use
 **Open your preferred text editor (e.g., VS Code).**

**Make sure the text editor window is active/focused.**

**Position your hand in front of the webcam clearly.**

**Perform one of the predefined finger gestures.**

**Watch the corresponding HTML tag typed automatically.**

**Press q in the video window to quit.**

---

### 🔮 Future Improvements
🤲 Support both hands and detect more complex gestures.

🆕 Add more HTML tags and CSS snippets for broader coding support.

🎨 Create a dedicated GUI with gesture guides and status.

🌐 Make it cross-platform and compatible with IDEs directly.

🧠 Integrate machine learning to recognize custom gestures.

🔊 Add audio feedback or haptic feedback for confirmation.

---
### 🧑‍💻 Contributing
Contributions are welcome! Feel free to:

Open issues for bugs or feature requests.

Submit pull requests with improvements or new gestures.

Share your use cases and feedback.

---

### 🙏 Acknowledgements
Thanks to MediaPipe for the amazing hand tracking solution.

Inspiration from various gesture-controlled input projects.

Open-source Python community for great libraries like OpenCV and PyAutoGUI.

***✨ Thank you for exploring this project! If you find it useful, please ⭐ star the repo and share it with fellow devs! ✨***

