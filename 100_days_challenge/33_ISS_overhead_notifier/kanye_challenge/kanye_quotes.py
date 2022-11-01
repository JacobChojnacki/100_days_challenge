import requests
import tkinter
from tkinter import messagebox


def get_quote():
    response = requests.get("https://api.kanye.rest")
    if response.raise_for_status():
        messagebox.showerror(title=f"{response.status_code}", message=response.raise_for_status())
    else:
        canvas.itemconfig(quote_text, text=response.json()['quote'])


# Create window
window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create Canvas
canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanyes quote", width=250)
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="kanye.png")
button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
button.grid(row=1, column=0)

window.mainloop()
