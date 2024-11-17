from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("1600x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=1600,height=1000)

window.resizable(False,False)

button1=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="black",corner_radius=38.62,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=1494.0000000000002,height=792)
button1.place(x=67,y=63)
label1=CTkLabel(frame,text="Login",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Helvetica",size=64,weight="bold"),width=0,height=28)
label1.place(x=702,y=97)
label2=CTkLabel(frame,text="Password:",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Helvetica",size=64,weight="bold"),width=0,height=28)
label2.place(x=254,y=518)
label3=CTkLabel(frame,text="Username:",text_color="white",fg_color="transparent",bg_color="black",corner_radius=0,font=CTkFont(family="Helvetica",size=64,weight="bold"),width=0,height=28)
label3.place(x=251,y=325)
entry4=CTkEntry(frame,text_color="white",fg_color="black",bg_color="black",corner_radius=19.48,font=CTkFont(family="Roboto",size=64,weight="normal"),border_width=1.0,border_color="#0049eb",width=780.2,height=108)
entry4.place(x=630,y=317)
entry5=CTkEntry(frame,text_color="white",fg_color="black",bg_color="black",corner_radius=19.48,font=CTkFont(family="Roboto",size=64,weight="normal"),border_width=1.0,border_color="#0049eb",width=780.2,height=108)
entry5.place(x=631,y=513)
button2=CTkButton(frame,text="Confirm",text_color="white",fg_color="black",bg_color="black",hover_color="blue",corner_radius=14,font=CTkFont(family="Helvetica",size=32,weight="bold"),border_width=1.1666666666666667,border_color="#0049eb",width=282.20000000000005,height=63)
button2.place(x=1237,y=761)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()