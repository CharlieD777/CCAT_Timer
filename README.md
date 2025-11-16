# CCAT_Timer
CCAT Timer is a Python/Tkinter app that helps users practice for the Criteria Cognitive Aptitude Test (CCAT) by simulating real exam pacing with visual and spoken countdown cues. It runs 50 questions with an 18-second timer each, recreating test pressure with automatic voice prompts.


CCAT Timer
CCAT Timer is a standalone Python/Tkinter application designed to help users practice for the Criteria Cognitive Aptitude Test (CCAT) by simulating real exam pacing through visual and spoken countdown cues. The timer runs 50 questions with an 18-second countdown per question, recreating test pressure using structured timing and automatic voice prompts.
Features
⏱ Visual Countdown
Large on-screen display
Shows Question Number and Seconds Remaining
Adjustable font sizes for easy visibility
🔊 Spoken Prompts (pyttsx3)
Announces “Problem X” at the start of each question
Announces “Ten seconds left” at the 10-second mark
Counts down 3, 2, 1 at the end of each question
Uses British female voice when available
🎛 Controls
Start / Stop toggle
Reset button (returns to Question 1 with full time)
⚙ Configuration
Adjustable variables at the top of the script:
Number of questions
Seconds per question
Font sizes for all UI elements
Installation
Requirements
Python 3.11 or later
Tkinter (included with Python on macOS/Windows)
pyttsx3 for TTS
pyobjc (macOS TTS backend)
Install dependencies
pip install pyttsx3 pyobjc
Run the app
python CCAT_Timer.py
Build as a Standalone App (macOS)
Requires Xcode command-line tools:
xcode-select --install
sudo xcodebuild -license
Then:
pyinstaller --windowed --onefile CCAT_Timer.py
Your .app will appear in the dist/ folder.
License
This project is unlicensed
Author
Created by Charles D Wintill.
For personal CCAT practice, timing improvement, and open community use.**
