from customtkinter import *
class GeneratorPage:
  def __init__(self, window):
    self.window=window
    self.window.title("Gui Generator")
    self.window.geometry("1800x1080")
    self.window.resizable(True,True)
    
    self.top_frame = CTkFrame(self.window, fg_color="transparent", corner_radius=15, height=100)
    self.top_frame.pack(fill="x", pady=10)

    self.sidebar_frame = CTkFrame(self.window, width=200, corner_radius=15, fg_color="#5ce1e6")
    self.sidebar_frame.pack(side="left", fill="y", padx=20, pady=10)

    
    
    self.menu_frame=CTkFrame(self.top_frame,fg_color="transparent")
    self.tool_frame = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)  

    self.canvas_frame = CTkFrame(self.window, fg_color="#a6a6a6")
    self.canvas_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)
    
    self.lastclick=None
    self.storebutton=[]
    self.currenton_widget=None
    self.color_window=None
    self.widget_button_page1()
    self.menu()
    self.tool()
    self.slider()
    
  def slider(self):
    self.slider_frame = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
    self.slider_frame.grid(row=0,column=2,padx=10 ,pady=10)
    self.sliderw = CTkSlider(self.slider_frame, from_=1, to=100, width=300,command=self.get_sliderxvalue)
    self.sliderw.grid(row=0, column=6, padx=10, pady=10)
    self.sliderw.set(1)
    self.widthlabel=CTkLabel(self.slider_frame,text=f"Width:{int(self.sliderw.get())}",text_color="black",bg_color="transparent")
    self.widthlabel.grid(row=0,column=5,padx=10)


    self.slider_framel = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
    self.slider_framel.grid(row=0,column=3,padx=10 ,pady=10)
    self.sliderl = CTkSlider(self.slider_framel, from_=1, to=100, width=300,command=self.get_slideryvalue)
    self.sliderl.grid(row=0, column=6, padx=10, pady=10)
    self.sliderl.set(1)
    self.lenghtlabel=CTkLabel(self.slider_framel,text=f"Length:{int(self.sliderl.get())}",text_color="black",bg_color="transparent")
    self.lenghtlabel.grid(row=0,column=5,padx=10)

    self.segmentedbuttonframe = CTkFrame(self.top_frame, fg_color="transparent", corner_radius=15, height=100)
    self.segmentedbuttonframe.grid(row=1,column=0,padx=10)

    self.background_button = CTkButton(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=40,text_color="black",text="Change Background Color",command=self.change_bg_color)
    self.background_button.grid(row=0,column=6,padx=10)

    self.sbutton=CTkSegmentedButton(self.segmentedbuttonframe,values=["Design","Code"],dynamic_resizing=True,height=30,corner_radius=20)
    self.sbutton.set("Design")
    self.sbutton.pack(pady=0,padx=10)

  def get_sliderxvalue(self,x):


    self.widthlabel.configure(text=f"Width: {int(x):02d}")


  def get_slideryvalue(self,x):
    self.lenghtlabel.configure(text=f"Width: {int(x):02d}")

  def change_bg_color(self):
      
      
      if self.color_window==None or not self.color_window.winfo_exists():
        self.color_window=CTkToplevel(self.window)
        self.color_window.resizable(False,False)
        self.color_window.title("Change Background Color")
        self.color_window.geometry("400x200")
        self.color_window.attributes('-topmost', True)
      
      self.colorbox=CTkComboBox(self.color_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","Custom"],command=self.colorapply)
      self.colorbox.place(relx=0.1,y=10)
      self.apply_custom_button=CTkButton(self.color_window,text="Apply",command=self.apply_color)
      self.apply_custom_button.place(relx=0.6,rely=0.8) 
      
      self.previewcolor=CTkFrame(self.color_window,width=150,height=100)
      self.previewcolor.place(relx=0.6,y=10)
  def apply_color(self):

    if self.colorbox.get()=="Custom":
      self.canvas_frame.configure(fg_color=self.custom_color.get())         
    else:
      self.canvas_frame.configure(fg_color=f"{self.colorbox.get().lower()}")                                         
  def colorapply(self,v):         
    if v=="Custom":
      self.custom_color=CTkEntry(self.color_window,text_color="gray")
      self.custom_color.insert(0, "Hex Color Code:")

      self.custom_color.place(relx=0.1,y=50)
      self.custom_color.bind("<FocusIn>",self.clear_entry)
      self.applycustomcolor=CTkButton(self.color_window,text="Apply To Preview",command=self.apply_to_preview)
      self.applycustomcolor.place(relx=0.1,y=90)
    else:
      try:
        self.applycustomcolor.destroy()
        self.custom_color.destroy()
      except:
        print("No Custom Color")
      self.previewcolor.configure(fg_color=f"{self.colorbox.get().lower()}")
  def clear_entry(self,e):
    self.custom_color.delete(0,END)
  def apply_to_preview(self):
    self.previewcolor.configure(fg_color=self.custom_color.get())
  def menu(self):
    self.export_button=CTkButton(self.menu_frame,text="Export",corner_radius=25,width=5,fg_color="#0097b2")
    self.export_button.grid(row=0,column=0,padx=5,pady=5)

    self.make_new_button=CTkButton(self.menu_frame,text="New",corner_radius=25,width=5,fg_color="#5ca16c")
    self.make_new_button.grid(row=0,column=1,padx=5,pady=5)

    self.save_button=CTkButton(self.menu_frame,text="Delete",corner_radius=25,width=5,fg_color="#ffbe5c",command=self.delete_widget)
    self.save_button.grid(row=0,column=2,padx=5,pady=5)
    self.menu_frame.grid(row=0,column=0)
  def tool(self):

    self.text=CTkLabel(self.tool_frame,text="Text:",fg_color="transparent",text_color="black")
    self.text.grid(row=0,column=1,padx=5,pady=5)
    self.entry1=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry1.grid(row=0,column=2,padx=5,pady=5)

    self.text2=CTkLabel(self.tool_frame,text="Command:",fg_color="transparent",text_color="black")
    self.text2.grid(row=0,column=3,padx=5,pady=5)
    self.entry2=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry2.grid(row=0,column=4,padx=5,pady=5)

    self.text3=CTkLabel(self.tool_frame,text="Currently On:",fg_color="transparent",text_color="black")
    self.text3.grid(row=0,column=6,padx=5,pady=5)
    self.entry3=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry3.grid(row=0,column=7,padx=5,pady=5)
    self.entry3.configure(state="disable")


    self.tool_frame.grid(row=0,column=1,padx=10 ,pady=10)
  def widget_button_page1(self):

    self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="Label", corner_radius=15,height=50)
    self.sidebar_button_2.pack(pady=10, padx=20)

    self.sidebar_button_3 = CTkButton(self.sidebar_frame, text="Button", corner_radius=15,height=50,command=self.addbutton)
    self.sidebar_button_3.pack(pady=10, padx=20)

    self.sidebar_button_4 = CTkButton(self.sidebar_frame, text="CheckBox", corner_radius=15,height=50)
    self.sidebar_button_4.pack(pady=10, padx=20)

    self.sidebar_button_5 = CTkButton(self.sidebar_frame, text="ComboBox", corner_radius=15,height=50)
    self.sidebar_button_5.pack(pady=10, padx=20)

    self.sidebar_button_6 = CTkButton(self.sidebar_frame, text="Entry", corner_radius=15,height=50)
    self.sidebar_button_6.pack(pady=10, padx=20)

    self.sidebar_button_7 = CTkButton(self.sidebar_frame, text="OptionMenu", corner_radius=15,height=50)
    self.sidebar_button_7.pack(pady=10, padx=20)

    self.sidebar_button_8 = CTkButton(self.sidebar_frame, text="ProgressBar", corner_radius=15,height=50)
    self.sidebar_button_8.pack(pady=10, padx=20)

    self.sidebar_button_9 = CTkButton(self.sidebar_frame, text="RadioButton", corner_radius=15,height=50)
    self.sidebar_button_9.pack(pady=10, padx=20)

    self.sidebar_button_10 = CTkButton(self.sidebar_frame, text="ScrollableFrame", corner_radius=15,height=50)
    self.sidebar_button_10.pack(pady=10, padx=20)

    self.sidebar_button_11 = CTkButton(self.sidebar_frame, text="SegmentedButton", corner_radius=15,height=50)
    self.sidebar_button_11.pack(pady=10, padx=20)

    self.sidebar_button_12 = CTkButton(self.sidebar_frame, text="Slider", corner_radius=15,height=50)
    self.sidebar_button_12.pack(pady=10, padx=20)

    self.sidebar_button_13 = CTkButton(self.sidebar_frame, text="Switch", corner_radius=15,height=50)
    self.sidebar_button_13.pack(pady=10, padx=20)

    self.sidebar_button_14 = CTkButton(self.sidebar_frame, text="TabView", corner_radius=15,height=50)
    self.sidebar_button_14.pack(pady=10, padx=20)
  def slider_start(self):
    self.sliderw.set(1)
    self.sliderl.set(1)
    self.widthlabel.configure(text=f"Width: {int(self.sliderw.get()):02d}")
    self.lenghtlabel.configure(text=f"Lenght: {int(self.sliderl.get()):02d}")
  def addbutton(self):
    self.button = CTkButton(self.canvas_frame, text="New-Button", corner_radius=15,bg_color="transparent")
    self.button.place(x=50,y=50)
    self.button.bind("<Button-1>",lambda e,widget=self.button:self.s_drag(e,widget))
    self.button.bind("<B1-Motion>",lambda e,widget=self.button:self.m_drag(e,widget))
    self.button.bind("<ButtonRelease-1>",lambda e,widget=self.button:self.r_drag(e,widget))
    self.button.bind("<Double-Button-1>",lambda e,widget=self.button:self.apply(e,widget))
    self.storebutton.append(self.button)
    self.slider_start()
  def addframe(self):
    self.newframe=CTkFrame(self.canvas_frame,fg_color="white")
    self.newframe.place(x=50,y=50)
    self.newframe.bind("<Button-1>",lambda e,widget=self.newframe:self.s_drag(e,widget))
    self.newframe.bind("<B1-Motion>",lambda e,widget=self.newframe:self.m_drag(e,widget))
    self.newframe.bind("<ButtonRelease-1>",lambda e,widget=self.newframe:self.r_drag(e,widget))
    self.newframe.bind("<Double-Button-1>",lambda e,widget=self.newframe:self.apply(e,widget))
    self.slider_start()

  def s_drag(self,e,widget):
    widget.start_xpos=e.x
    widget.start_ypos=e.y
    self.currenton_widget=widget
    
    
  def m_drag(self,e,widget):
    x=widget.winfo_x()-widget.start_xpos+e.x
    y=widget.winfo_y()-widget.start_ypos+e.y

    widget.place(x=x,y=y)
  def r_drag(self,e,widget):
    self.entry3.configure(state="normal")
    self.entry3.delete(0,END)
    self.entry3.insert(0,widget.cget("text"))
    self.entry3.configure(state="disable")
  def apply(self,e,widget):
    if len(self.entry1.get()) != 0:
      widget.configure(text=self.entry1.get())
      self.entry1.delete(0,END)
    widget.configure(height=int(self.sliderl.get())*9)
    widget.configure(width=int(self.sliderw.get())*16.6)
    print(widget.winfo_width())
    

  def delete_widget(self):
    if self.currenton_widget != None:
      self.currenton_widget.destroy()
    


    

    

set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = GeneratorPage(window)
window.mainloop()