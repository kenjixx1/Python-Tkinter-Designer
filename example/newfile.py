from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("400x300")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=400,height=300)

window.resizable(False,False)

button1=CTkButton(frame,text="New-Button",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=14,font=CTkFont(family="Helvetica",size=18),border_width=0,border_color="white",width=140,height=28)
button1.place(x=246,y=255)
label1=CTkLabel(frame,text="Login",text_color="black",fg_color="transparent",bg_color="#737373",corner_radius=0,font=CTkFont(family="Bold",size=32),width=0,height=28)
label1.place(x=162,y=14)
label2=CTkLabel(frame,text="Username:",text_color="black",fg_color="transparent",bg_color="#737373",corner_radius=0,font=CTkFont(family="Helvetica",size=18),width=0,height=28)
label2.place(x=71,y=102)
label3=CTkLabel(frame,text="Password:",text_color="black",fg_color="transparent",bg_color="#737373",corner_radius=0,font=CTkFont(family="Helvetica",size=18),width=0,height=28)
label3.place(x=74,y=164)
entry4=CTkEntry(frame,text_color="white",fg_color="black",bg_color="#737373",corner_radius=6,font=CTkFont(family="Roboto",size=13),border_width=0,border_color="white",width=140,height=28)
entry4.place(x=177,y=104)
entry5=CTkEntry(frame,text_color="white",fg_color="black",bg_color="#737373",corner_radius=6,font=CTkFont(family="Roboto",size=13),border_width=0,border_color="white",width=140,height=28)
entry5.place(x=177,y=166)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()