import time
import pyttsx3
import tkinter as tk

# ==================== CONFIGURATION ====================

# Countdown configuration
NUM_PROBLEMS = 50           # total number of questions/problems
SECONDS_PER_PROBLEM = 18    # seconds per question

# UI font sizes (can be tuned later or via a settings UI)
TOP_LINE_FONT_SIZE = 48     # "Question {#}"
SECOND_LINE_FONT_SIZE = 72  # seconds display
BUTTON_FONT_SIZE = 32       # Start/Stop button

# ==================== TEXT TO SPEECH SETUP ====================

# Initialize text-to-speech engine once
engine = pyttsx3.init()

# Try to set a British female voice if available
for v in engine.getProperty('voices'):
    name = v.name.lower()
    vid = v.id.lower()
    if ('en_gb' in vid or 'english' in name) and ('female' in name or 'fem' in vid):
        engine.setProperty('voice', v.id)
        break


def speak(text: str):
    engine.say(text)
    engine.runAndWait()


# ==================== GUI APPLICATION ====================

class CountdownApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CCAT Timer")

        # Core configuration
        self.num_problems = NUM_PROBLEMS
        self.seconds_per_problem = SECONDS_PER_PROBLEM

        # Fonts
        self.top_font = ("Helvetica", TOP_LINE_FONT_SIZE, "bold")
        self.second_font = ("Helvetica", SECOND_LINE_FONT_SIZE, "bold")
        self.button_font = ("Helvetica", BUTTON_FONT_SIZE)

        # State
        self.current_problem = 1
        self.seconds_left = self.seconds_per_problem
        self.running = False
        self.after_id = None

        # Layout
        self.question_label = tk.Label(
            self.root,
            text="",
            font=self.top_font
        )
        self.question_label.pack(pady=10)

        self.seconds_label = tk.Label(
            self.root,
            text="",
            font=self.second_font
        )
        self.seconds_label.pack(pady=10)

        self.start_button = tk.Button(
            self.root,
            text="Start",
            font=self.button_font,
            command=self.toggle_start_stop
        )
        self.start_button.pack(pady=20)

        # Reset button
        self.reset_button = tk.Button(
            self.root,
            text="Reset",
            font=self.button_font,
            command=self.reset
        )
        self.reset_button.pack(pady=10)

        self.update_display()

    # -------- UI helpers --------

    def update_display(self):
        self.question_label.config(text=f"Question {self.current_problem}")
        self.seconds_label.config(text=str(self.seconds_left))

    def toggle_start_stop(self):
        if self.running:
            self.stop()
        else:
            self.start()

    def start(self):
        if not self.running:
            self.running = True
            self.start_button.config(text="Stop")

            # If we've finished all problems and hit start again, reset
            if self.current_problem > self.num_problems:
                self.current_problem = 1
                self.seconds_left = self.seconds_per_problem

            # If seconds are at 0 for a problem, reset seconds
            if self.seconds_left <= 0:
                self.seconds_left = self.seconds_per_problem

            self.tick()

    def stop(self):
        self.running = False
        self.start_button.config(text="Start")
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

    def reset(self):
        # Stop timer if running
        self.stop()
        # Reset state
        self.current_problem = 1
        self.seconds_left = self.seconds_per_problem
        # Update display immediately
        self.update_display()

    # -------- Countdown logic --------

    def tick(self):
        if not self.running:
            return

        # Update labels
        self.update_display()

        # Voice prompts
        # At the start of each problem, announce the problem number
        if self.seconds_left == self.seconds_per_problem:
            speak(f"Problem {self.current_problem}")

        # At 10 seconds remaining, give a warning
        if self.seconds_left == 9:
            speak("Nine seconds left")

        # Last 3 seconds: 3, 2, 1
        if self.seconds_left in (3, 2, 1):
            speak(str(self.seconds_left))

        # Move state forward
        if self.seconds_left <= 1:
            # Advance to next problem or stop if done
            if self.current_problem < self.num_problems:
                self.current_problem += 1
                self.seconds_left = self.seconds_per_problem
            else:
                # Finished all problems
                self.stop()
                return
        else:
            self.seconds_left -= 1

        # Schedule next tick
        self.after_id = self.root.after(1000, self.tick)


if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
