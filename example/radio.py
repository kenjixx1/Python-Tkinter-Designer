from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("1600x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=1600,height=1000)

window.resizable(False,False)

Radio0=CTkRadioButton(frame,text="Option1",text_color="white",fg_color="black",bg_color="#737373",hover_color="gray",corner_radius=1000,font=CTkFont(family="Roboto",size=13,weight="normal"),border_color="white",width=100,height=22)
Radio0.place(x=196,y=107)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()