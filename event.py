import tkinter as tk
from tkinter import ttk


def display_price():
    """
    display beverage price function.
    :return: None
    """
    # print(2400)
    lbl_price.config(text=f"{2400} won")


def display_price_enter_key(e):
    display_price()


win = tk.Tk()
win.title('GUI 실습')
win.geometry('400x200')

lbl_price = tk.Label(win, text='?')
btn_menu = ttk.Button(win, text='Americano', command=display_price)
lbl_price.pack()
btn_menu.pack(fill='x')

win.bind("<Return>",  display_price_enter_key)

win.mainloop()