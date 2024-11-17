from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("1600x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=1600,height=1000)

window.resizable(False,False)

Swich0=CTkSwitch(frame,text="CTkSwitch",text_color="white",fg_color="white",bg_color="#737373",corner_radius=1000,font=CTkFont(family="Roboto",size=13,weight="normal"),border_width=3,border_color="transparent",width=100,height=24,progress_color="blue")
Swich0.place(x=255,y=201)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()