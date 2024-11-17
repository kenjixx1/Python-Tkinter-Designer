from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("400x300")
frame = CTkFrame(window,fg_color="black",
                bg_color="#e6e6ff",width=400,height=300,corner_radius=0)

window.resizable(False,False)

button1=CTkButton(frame,text="Confirm",text_color="white",fg_color="black",bg_color="black",hover_color="blue",corner_radius=14,font=CTkFont(family="Courier New",size=18,weight="bold"),border_width=1.3333333333333335,border_color="purple",width=140,height=45)
button1.place(x=244,y=242)
label1=CTkLabel(frame,text="Login",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Courier New",size=32,weight="bold"),width=0,height=28)
label1.place(x=150,y=13)
label2=CTkLabel(frame,text="Username:",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Courier New",size=32,weight="bold"),width=0,height=28)
label2.place(x=27,y=91)
label3=CTkLabel(frame,text="Password:",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Courier New",size=32,weight="bold"),width=0,height=28)
label3.place(x=30,y=152)
entry4=CTkEntry(frame,text_color="white",fg_color="black",bg_color="black",corner_radius=6,font=CTkFont(family="Courier New",size=24,weight="normal"),border_width=1.0,border_color="purple",width=166.0,height=36)
entry4.place(x=206,y=92)
entry5=CTkEntry(frame,text_color="white",show="*",fg_color="black",bg_color="black",corner_radius=6,font=CTkFont(family="Courier New",size=24,weight="normal"),border_width=1.0,border_color="purple",width=166.0,height=36)
entry5.place(x=206,y=156)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()