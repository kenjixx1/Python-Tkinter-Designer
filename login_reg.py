from customtkinter import *
import tkinter as tk

class Login:
  def __init__(self,window):
    self.window=window
    self.window.title("Login")
    self.window.geometry("500x350")
    self.window.resizable(False, False)
    # self.bbg_frame=CTkFrame(window,width=500,height=400,fg_color="#000000")
    self.bg_frame=CTkFrame(self.window,width=460,height=310,fg_color="#545454")
    self.frame=CTkFrame(self.bg_frame,width=440,height=290,fg_color="#737373")
    # self.bbg_frame.pack()
    self.bg_frame.grid(padx=20,pady=20)
    self.frame.grid(padx=10,pady=10)
    
    self.title_label("Login")
    self.login_pass()
    self.confirm_button()
    self.switch_button()


  def title_label(self,txt):
    txxt=tk.StringVar()
    txxt.set(txt)
    self.label=CTkLabel(self.frame,textvariable=txxt,font=("Arial",20,"bold"))
    self.label.place(relx=0.5, y=20, anchor="center")

  def login_pass(self):
    self.username=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",18,"bold"))
    self.username.place(relx=0.65, y=100, anchor="center")

    self.password=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",25,"bold"),show="*")
    self.password.place(relx=0.65, y=180, anchor="center")

    self.username_lable=CTkLabel(self.frame,text="Username:",font=("Arial",20,"bold"))
    self.username_lable.place(relx=0.27, y=100, anchor="center")

    self.password_lable=CTkLabel(self.frame,text="Password:",font=("Arial",20,"bold"))
    self.password_lable.place(relx=0.27, y=180, anchor="center")

  def confirm_button(self):

    self.confirm_button=CTkButton(self.frame,text="Login",corner_radius=20,width=90,height=45,fg_color="#0097b2",font=("Lexend",18,"bold"))
    self.confirm_button.place(relx=0.87, y=260, anchor="center")

  def reg_button(self):
    self.username=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",18,"bold"))
    self.username.place(relx=0.66, y=100, anchor="center")

    self.password=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",25,"bold"),show="*")
    self.password.place(relx=0.66, y=150, anchor="center")

    self.username_lable=CTkLabel(self.frame,text="Username:",font=("Arial",20,"bold"))
    self.username_lable.place(relx=0.28, y=100, anchor="center")

    self.password_lable=CTkLabel(self.frame,text="Password:",font=("Arial",20,"bold"))
    self.password_lable.place(relx=0.28, y=150, anchor="center")
  
    self.email=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",18,"bold"))
    self.email.place(relx=0.66, y=200, anchor="center")

    self.emailtxt=CTkLabel(self.frame,text="Email:",font=("Arial",20,"bold"))
    self.emailtxt.place(relx=0.33, y=200, anchor="center")
    

    
  def switch_button(self):
    self.switchbutton=CTkButton(self.frame,text="Create Account",font=("Lexend",18,"bold"),corner_radius=20,height=45,width=80,command=self.switch_reg)
    self.switchbutton.place(relx=0.21, y=260, anchor="center")



  def switch_reg(self):
    self.frame.destroy()
    self.frame=CTkFrame(self.bg_frame,width=440,height=290,fg_color="#737373")
    self.frame.grid(padx=10,pady=10)
    self.switch_button()
    self.reg_button()
    self.title_label("Register")
    


    
  def login(self):
    {}



    
  

  
      













set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = Login(window)
window.mainloop()