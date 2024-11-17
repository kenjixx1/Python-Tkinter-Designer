from customtkinter import *
import tkinter as tk

window = CTk()
window.geometry("1600x1000")
frame = CTkFrame(window,fg_color="#737373",
                bg_color="#040402",width=1600,height=1000)

window.resizable(False,False)

label0=CTkLabel(frame,text="New-Label",text_color="black",fg_color="transparent",bg_color="#737373",corner_radius=0,font=CTkFont(family="Helvetica",size=18,weight="bold"),width=0,height=28)
label0.place(x=50,y=50)
button1=CTkButton(frame,text="New-Button",text_color="white",fg_color="black",bg_color="#737373",hover_color="blue",corner_radius=14,font=CTkFont(family="Helvetica",size=18,weight="bold"),border_width=0,border_color="white",width=140,height=28)
button1.place(x=195,y=207)
checkbox2=CTkCheckBox(frame,text="NewCheckBox",text_color="black",fg_color="red",bg_color="#737373",hover_color="#0778ff",corner_radius=6,font=CTkFont(family="Roboto",size=13,weight="normal"),border_width=2,border_color="white",width=100,height=24,checkbox_width=24,checkbox_height=24)
checkbox2.place(x=77,y=164)
combobox3=CTkComboBox(frame,text_color="#ffffff",fg_color="black",bg_color="#737373",corner_radius=6,font=CTkFont(family="Roboto",size=13,weight="normal"),border_width=0,border_color="white",width=140,height=28,values=['-'])
combobox3.place(x=262,y=68)
entry4=CTkEntry(frame,text_color="white",fg_color="black",bg_color="#737373",corner_radius=6,font=CTkFont(family="Roboto",size=13,weight="normal"),border_width=0,border_color="white",width=140,height=28)
entry4.place(x=66,y=103)
OptionMenu5=CTkOptionMenu(frame,text_color="['#DCE4EE', '#DCE4EE']",fg_color="black",bg_color="#737373",corner_radius=6,font=CTkFont(family="Roboto",size=13,weight="normal"),width=140,height=28,values=['-'])
OptionMenu5.place(x=357,y=120)
progressbar6=CTkProgressBar(frame,fg_color="black",bg_color="#737373",corner_radius=1000,border_width=0,border_color="white",width=200,height=8,progress_color="#0166ff")
progressbar6.place(x=271,y=311)

frame8=CTkFrame(frame,fg_color="white",bg_color="#737373",corner_radius=6,border_width=0,border_color="white",width=200,height=200)
frame8.place(x=571,y=390)
sliderr9=CTkSlider(frame,fg_color="white",bg_color="#737373",corner_radius=1000,border_width=6,border_color="transparent",width=200,height=16,progress_color="blue")
sliderr9.place(x=219,y=501)
Swich10=CTkSwitch(frame,text="CTkSwitch",text_color="white",fg_color="white",bg_color="#737373",corner_radius=1000,font=CTkFont(family="Roboto",size=13,weight="normal"),border_width=3,border_color="transparent",width=100,height=24,progress_color="blue")
Swich10.place(x=136,y=588)

frame.pack()
set_appearance_mode("dark")
set_default_color_theme("blue") 
window.mainloop()