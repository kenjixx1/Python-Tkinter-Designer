from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("400x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=400,height=1000)

window.resizable(False,False)

button1=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button1.place(x=63,y=99)
button2=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button2.place(x=277,y=99)
button3=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button3.place(x=61,y=254)
button4=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button4.place(x=270,y=257)
button5=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button5.place(x=62,y=397)
button6=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button6.place(x=269,y=398)
button7=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button7.place(x=65,y=568)
button8=CTkButton(frame,text="",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=29.380000000000003,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=83.0,height=81)
button8.place(x=266,y=567)
button9=CTkButton(frame,text="New-Button",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=14,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=140,height=28)
button9.place(x=146,y=673)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()