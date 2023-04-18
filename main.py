import tkinter as tk
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")

# ---------------------UI SETUP----------------------- #
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=40, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=600, height=394)
card_front_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(300, 175, image=card_front_img)
canvas.create_text(300, 112, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(300, 197, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, pady=10)

cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image, borderwidth=0, highlightthickness=0)
unknown_button.grid(column=0, row=1)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(image=check_image, border=0, highlightthickness=0)
known_button.grid(column=1, row=1)

window.mainloop()
