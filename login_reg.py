from customtkinter import *

class Login:
  def __init__(self,window):
    self.window=window
    self.window.title("Login")
    self.window.geometry("500x400")
    self.window.resizable(False, False)
    # self.bbg_frame=CTkFrame(window,width=500,height=400,fg_color="#000000")
    self.bg_frame=CTkFrame(self.window,width=460,height=360,fg_color="#545454")
    self.frame=CTkFrame(self.bg_frame,width=440,height=340,fg_color="#737373")
    # self.bbg_frame.pack()
    self.bg_frame.grid(padx=20,pady=20)
    self.frame.grid(padx=10,pady=10)

    self.login_label()
    self.login_pass()

  def login_label(self):
    self.label=CTkLabel(self.frame,text="Login",font=("Arial",20,"bold"))
    self.label.place(relx=0.5, y=20, anchor="center")

  def login_pass(self):

    self.username=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",18,"bold"))
    self.username.place(relx=0.65, y=100, anchor="center")

    self.password=CTkEntry(self.frame,width=210,height=40,corner_radius=20,fg_color="#a6a6a6",border_width=5,text_color="white",font=("Lexend",25,"bold"),show="*")
    self.password.place(relx=0.65, y=170, anchor="center")

    self.username_lable=CTkLabel(self.frame,text="Username:",font=("Arial",20,"bold"))
    self.username_lable.place(relx=0.27, y=100, anchor="center")

    self.password_lable=CTkLabel(self.frame,text="Password:",font=("Arial",20,"bold"))
    self.password_lable.place(relx=0.27, y=170, anchor="center")

    
  

    
      













set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = Login(window)
window.mainloop()