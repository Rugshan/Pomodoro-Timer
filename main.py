# Imports
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown_mechanism(total_seconds):
    # Calculate Timer Minutes:Seconds
    minutes_remaining = int(total_seconds / 60)
    seconds_remaining = int(total_seconds % 60)

    # Update Clock Text
    canvas.itemconfigure(clock_text, text=f"{minutes_remaining:02}:{seconds_remaining:02}")

    # Recursively Countdown Until 0 Seconds
    if total_seconds > 0:
        window.after(1000, countdown_mechanism,
                     total_seconds - 1)  # Wait x amount of time, call function, passing it an argument (*args).


# ---------------------------- UI SETUP ------------------------------- #

# Create Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Title
title_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1, sticky="N")

# Canvas to Layer Widgets
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image((CANVAS_WIDTH / 2), (CANVAS_HEIGHT / 2), image=tomato_image)
canvas.grid(row=1, column=1)

# Clock Text
clock_text = canvas.create_text((CANVAS_WIDTH / 2),
                                ((CANVAS_HEIGHT / 2) + 30),
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))

# Update Digital Clock
countdown_mechanism(10)

# Start Button
start_button = Button(text="Start")
start_button.grid(row=2, column=0, sticky="E")

# Reset Button
start_button = Button(text="Reset")
start_button.grid(row=2, column=2, sticky="W")

# Checkmarks Label
checkmarks_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmarks_label.grid(row=3, column=1)

# Window Main Loop
window.mainloop()
