from customtkinter import *
import tkinter as tk
import tkinter.font as tkFont
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

    
    self.currenton_widget.configure(width=int(self.sliderw.get())*16.6)
    self.widthlabel.configure(text=f"Width: {int(x):02d}")


  def get_slideryvalue(self,x):
    self.currenton_widget.configure(height=int(self.sliderl.get())*9)
    self.lenghtlabel.configure(text=f"Lenght: {int(x):02d}")

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

    self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="Label", corner_radius=15,height=50,command=self.addlabel)
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
    self.button = CTkButton(self.canvas_frame, text="New-Button", corner_radius=15,bg_color="transparent",fg_color="black",text_color="white",hover_color="blue")
    self.button.place(x=50,y=50)
    self.button.bind("<Button-1>",lambda e,widget=self.button:self.s_drag(e,widget))
    self.button.bind("<B1-Motion>",lambda e,widget=self.button:self.m_drag(e,widget))
    self.button.bind("<ButtonRelease-1>",lambda e,widget=self.button:self.r_drag(e,widget))
    self.button.bind("<Double-Button-1>",lambda e,widget=self.button:self.apply(e,widget))
    self.button.bind("<Button-3>", lambda e,widget=self.button:self.show_properties_menu(e,widget))
    self.storebutton.append(self.button)
    self.slider_start()
  def addlabel(self):
    self.newlabel=CTkLabel(self.canvas_frame,fg_color="transparent",text="New-Label",text_color="black")
    self.newlabel.place(x=50,y=50)
    self.newlabel.bind("<Button-1>",lambda e,widget=self.newlabel:self.s_drag(e,widget))
    self.newlabel.bind("<B1-Motion>",lambda e,widget=self.newlabel:self.m_drag(e,widget))
    self.newlabel.bind("<ButtonRelease-1>",lambda e,widget=self.newlabel:self.r_drag(e,widget))
    self.newlabel.bind("<Double-Button-1>",lambda e,widget=self.newlabel:self.apply(e,widget))
    self.newlabel.bind("<Button-3>", lambda e,widget=self.newlabel:self.show_properties_menu(e,widget))
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
  def show_properties_menu(self,e,widget):
    self.entry3.configure(state="normal")
    self.entry3.delete(0,END)
    self.entry3.insert(0,widget.cget("text"))
    self.entry3.configure(state="disable")
    if len(self.entry1.get()) != 0:
      widget.configure(text=self.entry1.get())
      self.entry1.delete(0,END)
    self.currenton_widget=widget
    self.properties_menu = tk.Menu(self.canvas_frame, tearoff=0)
    self.properties_menu.add_command(label="Properties",command=self.show_properties)
    self.properties_menu.add_command(label="Apply",command=lambda e=None,widget=self.currenton_widget:self.apply(e,widget))
    self.properties_menu.add_separator()
    self.properties_menu.add_command(label="Delete",command=self.delete_widget)
    self.properties_menu.tk_popup(e.x_root, e.y_root)
  def delete_widget(self):
    if self.currenton_widget != None:
      self.currenton_widget.destroy()

  def show_properties(self):
    self.properties_window = CTkToplevel(self.canvas_frame)
    self.properties_window.attributes("-topmost",True)
    self.properties_window.geometry("700x500")
    self.properties_window.title("Properties")

    self.widget_color_label=CTkLabel(self.properties_window,text="Widget Color:")
    self.widget_color_label.grid(row=1,column=0,padx=10,pady=10)
    self.widget_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applywidgetcolor)
    self.widget_color.set(self.currenton_widget.cget("fg_color").capitalize())
    self.widget_color.grid(row=1,column=1,pady=10,padx=10)

    self.widget_text=CTkLabel(self.properties_window,text="Text:")
    self.widget_text.grid(row=0,column=0,pady=10,padx=10)
    self.widget_text_entry=CTkEntry(self.properties_window)
    self.widget_text_entry.grid(row=0,column=1)
    self.widget_text_entry.insert(0,self.currenton_widget.cget("text"))
    self.widget_text_entry.bind("<FocusIn>",lambda e:self.widget_text_entry.delete(0,END))
    self.widget_text_entry.bind("<Return>",self.apply_widget_text)

    self.text_color_label=CTkLabel(self.properties_window,text="Text Color:")
    self.text_color_label.grid(row=2,column=0,padx=10,pady=10)
    self.text_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applytextcolor)
    self.text_color.set(self.currenton_widget.cget("text_color").capitalize())
    self.text_color.grid(row=2,column=1,pady=10,padx=10)

    self.hovered_color_label=CTkLabel(self.properties_window,text="Hovered Color:")
    self.hovered_color_label.grid(row=3,column=0,padx=10,pady=10)
    try:
      self.hovered_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applyhovercolor)
      self.hovered_color.set(self.currenton_widget.cget("hover_color").capitalize())
      self.hovered_color.grid(row=3,column=1,pady=10,padx=10)
    except:
      self.hovered_color=CTkLabel(self.properties_window,text="Disabled")
      self.hovered_color.grid(row=3,column=1,padx=0,pady=10)

    self.corner_radius_label=CTkLabel(self.properties_window,text="Corner Radius:")
    self.corner_radius_label.grid(row=4,column=0,padx=10,pady=10)
    try:
      self.corner_radius = CTkSlider(self.properties_window, from_=1, to=100, width=150,command=self.applycornerradius)
      self.corner_radius.grid(row=4, column=1, padx=10, pady=10)
      self.corner_radius.set(self.currenton_widget.cget("corner_radius"))
    except:
      self.corner_radius=CTkLabel(self.properties_window,text="Disabled")
      self.corner_radius.grid(row=4,column=1,padx=0,pady=10)

    font = tkFont.Font(font=self.currenton_widget.cget("font"))
    size = font.cget("size")
    family = font.cget("family")

    self.font_label=CTkLabel(self.properties_window,text="Font")
    self.font_label.grid(row=5,column=0,padx=10,pady=10)
    self.font=CTkComboBox(self.properties_window,values=["Arial","Times New Roman","Helvetica","Courier New","Verdana ","Georgia ","Comic Sans MS","Tahoma","Lucida Grande"],command=self.changefont)
    self.font.grid(row=5,column=1,padx=10,pady=10)
    self.font.set(family.capitalize())

    self.font_size_label=CTkLabel(self.properties_window,text="Font")
    self.font_size_label.grid(row=5,column=2,padx=10,pady=10)
    self.font_size=CTkComboBox(self.properties_window,values=["2","4","8","12","14","16 ","18","24","32","64","128","256"],command=self.changefont)
    self.font_size.grid(row=5,column=3,padx=10,pady=10)
    self.font_size.set(size)

    self.font_style_label=CTkLabel(self.properties_window,text="Style")
    self.font_style_label.grid(row=5,column=4,padx=10,pady=10)
    self.font_style=CTkComboBox(self.properties_window,values=["None","Bold","Italic","Underline"],command=self.changefont)
    self.font_style.grid(row=5,column=5,padx=10,pady=10)



  def changefont(self,v):
    if self.font_style.get().lower()!="none":
      self.currenton_widget.configure(font=(v, int(self.font_size.get()),self.font_style.get().lower()))
    else:
      self.currenton_widget.configure(font=(v, int(self.font_size.get())))
  def applycornerradius(self,v):
    self.currenton_widget.configure(corner_radius=v)


  def apply_widget_text(self,e):
    self.currenton_widget.configure(text=self.widget_text_entry.get())
  def applywidgetcolor(self,v):
    if v=="Custom":
      self.custom_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_color.insert(0, "Hex Color Code:")

      self.custom_color.grid(row=1,column=2,pady=10,padx=10)
      self.custom_color.bind("<FocusIn>",self.clear_entry)
      self.applycustomcolor=CTkButton(self.properties_window,text="Apply",command=self.apply_widget_custom_color)
      self.applycustomcolor.grid(row=1,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_color.destroy()
        self.applycustomcolor.destroy()
      except:
        print("Error")
      color=self.widget_color.get().lower()
      self.currenton_widget.configure(fg_color=color)
  def apply_widget_custom_color(self):
    self.currenton_widget.configure(fg_color=self.custom_color.get())
  def applycustom_text_color(self):
    self.currenton_widget.configure(text_color=self.custom_text_color.get())
  def applytextcolor(self,v):
    if v=="Custom":
      self.custom_text_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_text_color.insert(0, "Hex Color Code:")
      self.custom_text_color.grid(row=2,column=2,pady=10,padx=10)
      self.custom_text_color.bind("<FocusIn>",lambda e:self.custom_text_color.delete(0,END))
      self.applycustom_text_color=CTkButton(self.properties_window,text="Apply",command=self.applycustom_text_color)
      self.applycustom_text_color.grid(row=2,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_text_color.destroy()
        self.applycustom_text_color.destroy()
      except:
        print("Error")
      color=self.text_color.get().lower()
      self.currenton_widget.configure(text_color=color)
    
    
  def applyhovercolor(self,v):
    if v=="Custom":
      self.custom_hovered_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_hovered_color.insert(0, "Hex Color Code:")
      self.custom_hovered_color.grid(row=3,column=2,pady=10,padx=10)
      self.custom_hovered_color.bind("<FocusIn>",lambda e:self.custom_hovered_color.delete(0,END))
      self.applycustom_hovered_color=CTkButton(self.properties_window,text="Apply",command=self.applycustom_hover_color)
      self.applycustom_hovered_color.grid(row=3,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_hovered_color.destroy()
        self.applycustom_hovered_color.destroy()
      except:
        print("Error")
      color=self.hovered_color.get().lower()
      self.currenton_widget.configure(hover_color=color)

  def applycustom_hover_color(self):
    self.currenton_widget.configure(hover_color=self.custom_hovered_color.get())

set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = GeneratorPage(window)
window.mainloop()