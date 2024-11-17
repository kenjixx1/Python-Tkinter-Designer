from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("1600x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=1600,height=1000)

window.resizable(False,False)

sliderr0=CTkSlider(frame,fg_color="white",bg_color="#737373",corner_radius=1000,border_width=6,border_color="transparent",width=200,height=16,progress_color="blue")
sliderr0.place(x=164,y=282)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()