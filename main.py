# Imports
from tkinter import Tk, Canvas, PhotoImage, Label, Button

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SECS = 25 * 60
SHORT_BREAK_SECS = 5 * 60
LONG_BREAK_SECS = 20 * 60
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224

# Global Variable
rep_counter = 0


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global rep_counter
    rep_counter = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global rep_counter
    rep_counter += 1

    if rep_counter in range(1, 8, 2):
        countdown_mechanism(5)
    elif rep_counter in range(2, 7, 2):
        checkmarks_label.config(text=f"{'✔' * int((rep_counter / 2))}")
        countdown_mechanism(2)
    elif rep_counter == 8:
        checkmarks_label.config(text=f"{'✔' * 4}")
        countdown_mechanism(10)



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
    elif rep_counter <= 8:
        start_timer()


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

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0, sticky="E")

# Reset Button
start_button = Button(text="Reset", command=timer_reset)
start_button.grid(row=2, column=2, sticky="W")


# Checkmarks Label
checkmarks_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmarks_label.grid(row=3, column=1)

# Window Main Loop
window.mainloop()
