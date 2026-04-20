# autoclickergui.py

from tkinter import *
import autoclicker as ac
import threading

window = Tk()
window.geometry("420x210")
window.title("Auto Clicker")
window.configure(bg="#333333")
window.resizable(False, False)
window.iconbitmap("mesmerizerteto.ico")


def save_delay():
    ac.set_delay(e1.get())


def save_click_type():
    ac.set_click_type(click_option.get())


# center container
center_frame = Frame(window, bg="#333333")
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


# LEFT SIDE = Delay
delay_frame = Frame(center_frame, bg="#333333")
delay_frame.pack(side=LEFT, padx=20)

e1 = Entry(
    delay_frame,
    bg="#333333",
    fg="#FFFFFF",
    insertbackground="#FFFFFF",
    width=15
)
e1.pack(pady=10)

Button(
    delay_frame,
    text="Set Click Delay",
    command=save_delay,
    bg="#333333",
    fg="#FF3399",
    activebackground="#444444",
    activeforeground="#FF3399"
).pack()


# RIGHT SIDE = Click Type
click_frame = Frame(center_frame, bg="#333333")
click_frame.pack(side=RIGHT, padx=20)

click_option = StringVar()
click_option.set("left")

dropdown = OptionMenu(
    click_frame,
    click_option,
    "left",
    "right"
)

dropdown.config(
    bg="#333333",
    fg="#FFFFFF",
    activebackground="#444444",
    activeforeground="#FFFFFF",
    highlightthickness=0,
    width=10
)

dropdown["menu"].config(
    bg="#333333",
    fg="#FFFFFF"
)

dropdown.pack(pady=10)

Button(
    click_frame,
    text="Set Click Type",
    command=save_click_type,
    bg="#333333",
    fg="#FF3399",
    activebackground="#444444",
    activeforeground="#FF3399"
).pack()


threading.Thread(target=ac.run, daemon=True).start()

window.mainloop()