from customtkinter import *
import tkinter as tk
import tkinter.font as tkFont
from export import export
import colorpicker 
from tkinter import filedialog
class GeneratorPage:
  def __init__(self, window):
    
    self.magnet=IntVar()
    self.clipboard=None
    self.window=window
    self.window.title("Gui Generator")
    self.window.geometry("1800x1080")
    self.window.resizable(True,True)
    
    #Theme
    self.theme="Dark"
    self.sidebar_button_color="#fefbc8"
    self.sidebar_button_text_color="#294d87"
    self.sidebar_button_hover_color="#fefde8"
    self.window_color="#e6e6ff"
    self.sidebar_frame_color="#f5c8c5"
    self.top_frame_color="#9bfaf7"
    self.canvas_frame_color="#fcf6e1"
    self.menu_frame_color="transparent"

    self.window.configure(fg_color=self.window_color)

    self.allsidebuttons=[]
    self.menulist=[]
    self.alltopfrape=[]
    self.alltext=[]
    self.allslider=[]
    self.allentry=[]
    self.segmentedbutton=None

    self.top_frame = CTkFrame(self.window, fg_color="transparent", corner_radius=15, height=100)
    self.top_frame.pack(fill="x", pady=10)

    self.sidebar_frame = CTkFrame(self.window, width=200, corner_radius=15, fg_color=self.sidebar_frame_color)
    self.sidebar_frame.pack(side="left", fill="y", padx=20, pady=10)

    
    
    self.menu_frame=CTkFrame(self.top_frame,fg_color="transparent",corner_radius=20)
    self.tool_frame = CTkFrame(self.top_frame, fg_color=self.top_frame_color, corner_radius=15, height=100)  
    self.alltopfrape.append(self.tool_frame)

    self.canvas_frame = CTkFrame(self.window, fg_color="#fcf6e1",width=1600, height=1000)
    self.canvas_frame.bind("<Button-3>",self.show_canvas_properties_menu)
    self.canvas_frame.pack(side="right", expand=True, padx=20, pady=20)

   



    self.window.bind("<Control-c>",self.copy)
    self.window.bind("<Control-v>",self.paste)
    
    self.canvas_frame.bind("<Button-1>",self.clear)
    
    self.default_font=CTkFont(family="Helvetica", size=18, weight="bold")

    self.lastclick=None
    self.storebutton=[]
    self.currenton_widget=None
    self.color_window=None
    self.widget_button_page1()
    self.menu()
    self.tool()
    self.slider()
    self.change_theme(self.theme)
  def clear(self,e):
    e.widget.master.focus_set()
    self.currenton_widget=None
    self.entry1.configure(state="normal")
    self.entry1.delete(0,END)
    self.entry3.configure(state="normal")
    self.entry3.delete(0,END)
     
  def on_focus_out(self,e):
    self.currenton_widget=None

  def slider(self):
    self.slider_frame = CTkFrame(self.top_frame, fg_color=self.top_frame_color, corner_radius=15, height=100)
    self.slider_frame.grid(row=0,column=2,padx=10 ,pady=10)
    self.sliderw = CTkSlider(self.slider_frame, from_=1, to=100, width=300,command=self.get_sliderxvalue)
    self.sliderw.grid(row=0, column=6, padx=10, pady=10)
    self.sliderw.set(1)
    self.widthlabel=CTkLabel(self.slider_frame,text=f"Width:{int(self.sliderw.get())}",text_color="black",bg_color="transparent")
    self.widthlabel.grid(row=0,column=5,padx=10)

    


    self.slider_framel = CTkFrame(self.top_frame, fg_color=self.top_frame_color, corner_radius=15, height=100)
    self.slider_framel.grid(row=0,column=3,padx=10 ,pady=10)
    self.sliderl = CTkSlider(self.slider_framel, from_=1, to=100, width=300,command=self.get_slideryvalue)
    self.sliderl.grid(row=0, column=6, padx=10, pady=10)
    self.sliderl.set(1)
    self.lenghtlabel=CTkLabel(self.slider_framel,text=f"Length:{int(self.sliderl.get())}",text_color="black",bg_color="transparent")
    self.lenghtlabel.grid(row=0,column=5,padx=10)

    self.allslider.append(self.sliderw)
    self.allslider.append(self.sliderl)

    self.segmentedbuttonframe = CTkFrame(self.top_frame, fg_color="transparent", corner_radius=15, height=100)
    self.segmentedbuttonframe.grid(row=1,column=0,padx=10)

    self.background_button = CTkButton(self.top_frame, fg_color="#9bfaf7", corner_radius=15, height=40,text_color="black",text="Setting",command=self.canvas_setting)
    self.background_button.grid(row=0,column=6,padx=10)

    self.sbutton=CTkSegmentedButton(self.segmentedbuttonframe,values=["Light","Dark"],dynamic_resizing=False,height=30,corner_radius=10,command=self.change_theme,width=100)
    self.sbutton.set("Dark")
    self.sbutton.pack(pady=0,padx=10)
    self.segmentedbutton=self.sbutton

    self.alltext.append(self.widthlabel)
    self.alltext.append(self.lenghtlabel)

    self.alltopfrape.append(self.slider_frame)
    self.alltopfrape.append(self.slider_framel)
    self.alltopfrape.append(self.segmentedbuttonframe)

  def change_theme(self,v):
    
    if v=="Light":
      self.sidebar_button_color="#fefbc8"
      self.sidebar_button_text_color="#294d87"
      self.sidebar_button_hover_color="#fefde8"
      self.window_color="#e6e6ff"
      self.sidebar_frame_color="#f5c8c5"
      self.top_frame_color="#f5c8c5"
      self.canvas_frame_color="#fcf6e1"
      self.menu_frame_color="#f5c8c5"
      
      for button in self.allsidebuttons:
        button.configure(fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
      for text in self.alltext:
        text.configure(text_color=self.sidebar_button_text_color)
      for frame in self.alltopfrape:#Testing
        frame.configure(fg_color=self.top_frame_color)
      for entry in self.allentry:
        entry.configure(fg_color="#fcf5f4",text_color="#294d87",border_color="#f0b5b1",border_width=2)
      for slider in self.allslider:
        slider.configure(fg_color="#fcf5f4",progress_color="#fefbc8",button_color="#e68983")

      self.segmentedbutton.configure(selected_color="#fefbc8",unselected_color="#f5c8c5",text_color="#294d87",fg_color="#f5c8c5")
      self.window.configure(fg_color=self.window_color)
      self.sidebar_frame.configure(fg_color=self.sidebar_frame_color)
      self.canvas_frame.configure(fg_color=self.canvas_frame_color)
      self.menu_frame.configure(fg_color=self.menu_frame_color)
      

    else:
      self.sidebar_button_color="#0166ff"
      self.sidebar_button_text_color="#ffffff"
      self.sidebar_button_hover_color="#0778ff"
      self.window_color="#040402"
      self.sidebar_frame_color="#101116"
      self.top_frame_color="#101116"
      self.canvas_frame_color="#737373"
      self.menu_frame_color="#101116"

      for button in self.allsidebuttons:
        button.configure(fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
      for text in self.alltext:
        text.configure(text_color=self.sidebar_button_text_color)
      for frame in self.alltopfrape:#Testing
        frame.configure(fg_color=self.top_frame_color)
      for slider in self.allslider:
        slider.configure(fg_color="#383840",progress_color="#1153b0",button_color="#ceced0")

      for entry in self.allentry:
        entry.configure(fg_color="#23232b",text_color="#ffffff",border_color="#28467b",border_width=2)
      
      self.segmentedbutton.configure(selected_color="#0166ff",unselected_color="#101116",text_color="#ffffff",fg_color="#0166ff",border_width=1)
      

      self.window.configure(fg_color=self.window_color)
      self.sidebar_frame.configure(fg_color=self.sidebar_frame_color)
      self.canvas_frame.configure(fg_color=self.canvas_frame_color)
      self.menu_frame.configure(fg_color=self.menu_frame_color)

  def get_sliderxvalue(self,x):

    if type(self.currenton_widget)==CTkCheckBox:
      self.currenton_widget.configure(checkbox_width=int(self.sliderw.get())*16)
    else:
      self.currenton_widget.configure(width=int(self.sliderw.get())*16)
    self.widthlabel.configure(text=f"Width: {int(x):02d}")


  def get_slideryvalue(self,x):
    
    if type(self.currenton_widget)==CTkCheckBox:
      self.currenton_widget.configure(checkbox_height=int(self.sliderl.get())*10)
    else:
      self.currenton_widget.configure(height=int(self.sliderl.get())*10)
    self.lenghtlabel.configure(text=f"Lenght: {int(x):02d}")

  def canvas_setting(self):
      
      
      if self.color_window==None or not self.color_window.winfo_exists():
        self.color_window=CTkToplevel(self.window)
        self.color_window.resizable(False,False)
        self.color_window.title("Setting")
        self.color_window.geometry("600x400")
        self.color_window.attributes('-topmost', True)
      
      self.colorbox=CTkComboBox(self.color_window,values=["Default","Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","Custom"],command=self.colorapply)
      self.colorbox.place(relx=0.7,y=10)
      self.apply_custom_button=CTkButton(self.color_window,text="Apply Color",command=self.apply_color)
      self.apply_custom_button.place(relx=0.4,y=120) 
      
      widthlabel=CTkLabel(self.color_window,text="Width:",fg_color="transparent",text_color="white")
      widthlabel.place(x=15,y=10)
      heightlabel=CTkLabel(self.color_window,text="Height:",fg_color="transparent",text_color="white")
      heightlabel.place(x=15,y=60)
      self.widthentry=CTkEntry(self.color_window,fg_color="gray")
      self.widthentry.insert(0, "1600")
      self.widthentry.place(x=60,y=10)
      self.heightentry=CTkEntry(self.color_window,fg_color="gray")
      self.heightentry.insert(0, "1000")
      self.heightentry.place(relx=0.1,y=60)

      
      self.check_magnet=CTkCheckBox(self.color_window,text="Magnet",variable=self.magnet)
      self.check_magnet.place(x=430,y=50)
      self.magnetnum=CTkSlider(self.color_window,width=100,from_=1, to=20,command=self.roundmag)
      self.magnetnum.set(10)
      self.magnetnum.place(x=420,y=80)


      self.applysize=CTkButton(self.color_window,text="Apply Size",command=self.apply_size)
      self.applysize.place(relx=0.1,y=100)

      self.previewcolor=CTkFrame(self.color_window,width=150,height=100,fg_color=self.canvas_frame.cget("fg_color"))
      self.previewcolor.place(relx=0.4,y=10)
  def roundmag(self,x):
    self.magnetnum.set(round(x))
  def apply_size(self):
    self.canvas_frame.configure(width=int(self.widthentry.get()),height=int(self.heightentry.get()))
  def apply_color(self):
    if self.colorbox.get()=="Custom":
      self.canvas_frame.configure(fg_color=self.custom_color.get())
    elif self.colorbox.get()=="Default":
      self.canvas_frame.configure(fg_color="#fcf6e1")         
    else:
      self.canvas_frame.configure(fg_color=f"{self.colorbox.get().lower()}")                                         
  def colorapply(self,v):         
    if v=="Custom":
      self.custom_color=CTkEntry(self.color_window,text_color="gray")
      self.custom_color.insert(0, "Hex Color Code:")

      self.custom_color.place(relx=0.1,y=140)
      self.custom_color.bind("<FocusIn>",self.clear_entry)
      self.applycustomcolor=CTkButton(self.color_window,text="Apply To Preview",command=self.apply_to_preview)
      self.applycustomcolor.place(relx=0.1,y=180)
    elif v=="Default":
      self.previewcolor.configure(fg_color=f"#fcf6e1")
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
    self.export_button=CTkButton(self.menu_frame,text="Export",corner_radius=25,width=5,fg_color="#0097b2",command=self.show_export_menu)
    self.export_button.grid(row=0,column=0,padx=5,pady=5)

    self.make_new_button=CTkButton(self.menu_frame,text="New",corner_radius=25,width=5,fg_color="#5ca16c",command=self.new)
    self.make_new_button.grid(row=0,column=1,padx=5,pady=5)

    self.save_button=CTkButton(self.menu_frame,text="Delete",corner_radius=25,width=5,fg_color="#ffbe5c",command=self.delete_widget)
    self.save_button.grid(row=0,column=2,padx=5,pady=5)
    self.menu_frame.grid(row=0,column=0,padx=5)


    self.allsidebuttons.append(self.export_button)
    self.allsidebuttons.append(self.make_new_button)
    self.allsidebuttons.append(self.save_button)
  def new(self):
    for widget in self.canvas_frame.winfo_children():
      widget.destroy()

  def show_export_menu(self):
    self.export_window = CTkToplevel(self.window)
    self.export_window.attributes("-topmost",True)
    self.export_window.geometry("400x200")
    self.export_window.title("Export")

    self.export_frame = CTkFrame(self.export_window, fg_color="#040402", corner_radius=15, height=100)
    self.label=CTkLabel(self.export_frame,text="File Name:",fg_color="transparent",text_color="white")
    self.label.place(x=80,y=10)
    self.entry=CTkEntry(self.export_frame,fg_color="#040402",corner_radius=15,border_color="#0166ff",border_width=2)
    self.entry.place(x=150,y=10)

    self.export_button=CTkButton(self.export_frame,text="Export",corner_radius=15,fg_color="#5ca16c",command=lambda:self.export(self.entry.get()))
    self.export_button.place(x=210,y=120)

    self.export_frame.pack(fill="both", expand=True, padx=20, pady=20)
  def export(self,name):
    if not name:
      CTkLabel(self.export_frame,text="Please enter a file name!",text_color="red").place(x=80,y=50)
      return
    self.export_window.attributes("-topmost",False)
    file_path = filedialog.asksaveasfilename(
            title="Select Export Location",
            initialfile=name,
            defaultextension=".py",
            filetypes=(("Python Files", "*.py"), ("All Files", "*.*"))
        )
    if file_path:
      export(self.canvas_frame,file_path)
      CTkLabel(self.export_frame,text=f"File saved to {file_path}",text_color="green").place(x=80,y=80)
      

  def tool(self):

    self.text=CTkLabel(self.tool_frame,text="Text:",fg_color="transparent",text_color="black")
    self.text.grid(row=0,column=1,padx=5,pady=5)
    self.entry1=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry1.grid(row=0,column=2,padx=5,pady=5)
    self.entry1.bind("<Return>",self.apply_widget_text2)

    self.text2=CTkLabel(self.tool_frame,text="Command:",fg_color="transparent",text_color="black")
    self.text2.grid(row=0,column=3,padx=5,pady=5)
    self.entry2=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry2.grid(row=0,column=4,padx=5,pady=5)

    self.text3=CTkLabel(self.tool_frame,text="Currently On:",fg_color="transparent",text_color="black")
    self.text3.grid(row=0,column=6,padx=5,pady=5)
    self.entry3=CTkEntry(self.tool_frame,fg_color="#a6a6a6",corner_radius=15)
    self.entry3.grid(row=0,column=7,padx=5,pady=5)
    self.entry3.configure(state="disable")
    
    
    self.allentry.append(self.entry1)
    self.allentry.append(self.entry2)
    self.allentry.append(self.entry3)

    self.alltext.append(self.text)
    self.alltext.append(self.text2)
    self.alltext.append(self.text3)


    self.tool_frame.grid(row=0,column=1,padx=10 ,pady=10)
  def widget_button_page1(self):
    allbutton=[]
    self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="Label", corner_radius=15,height=50,command=self.addlabel,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_2.pack(pady=10, padx=20)
    

    self.sidebar_button_3 = CTkButton(self.sidebar_frame, text="Button", corner_radius=15,height=50,command=self.addbutton,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_3.pack(pady=10, padx=20)

    self.sidebar_button_4 = CTkButton(self.sidebar_frame, text="CheckBox", corner_radius=15,height=50,command=self.addcheckbox,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_4.pack(pady=10, padx=20)

    self.sidebar_button_5 = CTkButton(self.sidebar_frame, text="ComboBox", corner_radius=15,height=50,command=self.addcombobox,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_5.pack(pady=10, padx=20)

    self.sidebar_button_6 = CTkButton(self.sidebar_frame, text="Entry", corner_radius=15,height=50,command=self.addentry,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_6.pack(pady=10, padx=20)

    self.sidebar_button_7 = CTkButton(self.sidebar_frame, text="OptionMenu", corner_radius=15,height=50,command=self.addoptionmenu,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_7.pack(pady=10, padx=20)

    self.sidebar_button_8 = CTkButton(self.sidebar_frame, text="ProgressBar", corner_radius=15,height=50,command=self.addprogressbar,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_8.pack(pady=10, padx=20)

    self.sidebar_button_9 = CTkButton(self.sidebar_frame, text="RadioButton", corner_radius=15,height=50,command=self.addradiobutton,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_9.pack(pady=10, padx=20)

    self.sidebar_button_10 = CTkButton(self.sidebar_frame, text="Frame", corner_radius=15,height=50,command=self.addframe,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_10.pack(pady=10, padx=20)

    self.sidebar_button_12 = CTkButton(self.sidebar_frame, text="Slider", corner_radius=15,height=50,command=self.addslider,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_12.pack(pady=10, padx=20)

    self.sidebar_button_13 = CTkButton(self.sidebar_frame, text="Switch", corner_radius=15,height=50,command=self.addswitch,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_13.pack(pady=10, padx=20)

    self.sidebar_button_14 = CTkButton(self.sidebar_frame, text="Color Finder", corner_radius=15,height=50,command=colorpicker.pickcolor,fg_color=self.sidebar_button_color,text_color=self.sidebar_button_text_color,hover_color=self.sidebar_button_hover_color)
    self.sidebar_button_14.pack(pady=10, padx=20)

    
    self.allsidebuttons.append(self.sidebar_button_2)
    self.allsidebuttons.append(self.sidebar_button_3)
    self.allsidebuttons.append(self.sidebar_button_4)
    self.allsidebuttons.append(self.sidebar_button_5)
    self.allsidebuttons.append(self.sidebar_button_6)
    self.allsidebuttons.append(self.sidebar_button_7)
    self.allsidebuttons.append(self.sidebar_button_8)
    self.allsidebuttons.append(self.sidebar_button_9)
    self.allsidebuttons.append(self.sidebar_button_10)
    self.allsidebuttons.append(self.sidebar_button_12)
    self.allsidebuttons.append(self.sidebar_button_13)
    self.allsidebuttons.append(self.sidebar_button_14)
    

    

    
  def slider_start(self):
    self.sliderw.set(1)
    self.sliderl.set(1)
    self.widthlabel.configure(text=f"Width: {int(self.sliderw.get()):02d}")
    self.lenghtlabel.configure(text=f"Lenght: {int(self.sliderl.get()):02d}")
  def addbutton(self,properties=None,master=None):
    if properties==None:
      self.button = CTkButton(self.canvas_frame, text="New-Button", corner_radius=15,bg_color="transparent",fg_color="black",text_color="white",hover_color="blue",border_color="white",font=self.default_font)
      self.button.place(x=0,y=0)
    else:
      if master!=None:
        self.button = CTkButton(master, **properties)
        self.button.place(x=50,y=50)
        self.button.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.button = CTkButton(self.canvas_frame, **properties)
        self.button.place(x=50,y=50)

        
    self.button.bind("<Button-1>",lambda e,widget=self.button:self.s_drag(e,widget))
    self.button.bind("<B1-Motion>",lambda e,widget=self.button:self.m_drag(e,widget))
    self.button.bind("<ButtonRelease-1>",lambda e,widget=self.button:self.r_drag(e,widget))
    self.button.bind("<Double-Button-1>",lambda e,widget=self.button:self.apply(e,widget))
    self.button.bind("<Button-3>", lambda e,widget=self.button:self.show_properties_menu(e,widget))
    self.storebutton.append(self.button)
    self.slider_start()
  def addlabel(self,properties=None,master=None):
    if properties==None:
      self.newlabel=CTkLabel(self.canvas_frame,fg_color="transparent",text="New-Label",text_color="black",font=self.default_font)
      self.newlabel.place(x=50,y=50)
    else:
      if master!=None:
        self.newlabel = CTkLabel(master, **properties)
        self.newlabel.place(x=50,y=50)
        self.newlabel.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newlabel = CTkLabel(self.canvas_frame, **properties)
        self.newlabel.place(x=50,y=50)

    self.newlabel.bind("<Button-1>",lambda e,widget=self.newlabel:self.s_drag(e,widget))
    self.newlabel.bind("<B1-Motion>",lambda e,widget=self.newlabel:self.m_drag(e,widget))
    self.newlabel.bind("<ButtonRelease-1>",lambda e,widget=self.newlabel:self.r_drag(e,widget))
    self.newlabel.bind("<Double-Button-1>",lambda e,widget=self.newlabel:self.apply(e,widget))
    self.newlabel.bind("<Button-3>", lambda e,widget=self.newlabel:self.show_properties_menu(e,widget))
    self.slider_start()

  def addcheckbox(self,properties=None,master=None):
    if properties==None:
      self.newcheckbox=CTkCheckBox(self.canvas_frame,text="NewCheckBox",text_color="black",fg_color="red",hover_color=self.sidebar_button_hover_color,border_color="white",border_width=2)
      self.newcheckbox.place(x=50,y=50)
    else:
      if master!=None:
        self.newcheckbox = CTkCheckBox(master, **properties)
        self.newcheckbox.place(x=50,y=50)
        self.newcheckbox.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newcheckbox = CTkCheckBox(self.canvas_frame, **properties)
        self.newcheckbox.place(x=50,y=50)
    self.newcheckbox.bind("<Button-1>",lambda e,widget=self.newcheckbox:self.s_drag(e,widget))
    self.newcheckbox.bind("<B1-Motion>",lambda e,widget=self.newcheckbox:self.m_drag(e,widget))
    self.newcheckbox.bind("<ButtonRelease-1>",lambda e,widget=self.newcheckbox:self.r_drag(e,widget))
    self.newcheckbox.bind("<Double-Button-1>",lambda e,widget=self.newcheckbox:self.apply(e,widget))
    self.newcheckbox.bind("<Button-3>", lambda e,widget=self.newcheckbox:self.show_properties_menu(e,widget))

  def addcombobox(self,properties=None,master=None):
    if properties==None:
      self.newcombobox=CTkComboBox(self.canvas_frame,fg_color="black",values=["-"],state="readonly",text_color=self.sidebar_button_text_color,border_color="white")
      self.newcombobox.place(x=50,y=50)
    else:
      if master!=None:
        self.newcombobox = CTkComboBox(master, **properties)
        self.newcombobox.place(x=50,y=50)
        self.newcombobox.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newcombobox = CTkComboBox(self.canvas_frame, **properties)
        self.newcombobox.place(x=50,y=50)

    self.newcombobox.bind("<Button-1>",lambda e,widget=self.newcombobox:self.s_drag(e,widget))
    self.newcombobox.bind("<B1-Motion>",lambda e,widget=self.newcombobox:self.m_drag(e,widget))
    self.newcombobox.bind("<ButtonRelease-1>",lambda e,widget=self.newcombobox:self.r_drag(e,widget))
    self.newcombobox.bind("<Double-Button-1>",lambda e,widget=self.newcombobox:self.apply(e,widget))
    self.newcombobox.bind("<Button-3>", lambda e,widget=self.newcombobox:self.show_properties_menu(e,widget))
  def addentry(self,properties=None,master=None):
    if properties==None:
      self.newentry=CTkEntry(self.canvas_frame,fg_color="black",text_color="white",border_color="white",border_width=0)
      self.newentry.place(x=50,y=50)
    else:
      if master!=None:
        self.newentry = CTkEntry(master, **properties)
        self.newentry.place(x=50,y=50)
        self.newentry.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newentry = CTkEntry(self.canvas_frame, **properties)
        self.newentry.place(x=50,y=50)
    self.newentry.bind("<Button-1>",lambda e,widget=self.newentry:self.s_drag(e,widget))
    self.newentry.bind("<B1-Motion>",lambda e,widget=self.newentry:self.m_drag(e,widget))
    self.newentry.bind("<ButtonRelease-1>",lambda e,widget=self.newentry:self.r_drag(e,widget))
    self.newentry.bind("<Double-Button-1>",lambda e,widget=self.newentry:self.apply(e,widget))
    self.newentry.bind("<Button-3>", lambda e,widget=self.newentry:self.show_properties_menu(e,widget))
    self.entnewentryry1.bind("<FocusOut>", self.on_focus_out)

  def addoptionmenu(self,properties=None,master=None):
    if properties==None:
      self.newoptionmenu=CTkOptionMenu(self.canvas_frame,fg_color="black",values=["-"],state="readonly",dynamic_resizing=True,text_color="black")
      self.newoptionmenu.place(x=50,y=50)
    else:
      if master!=None:
        self.newoptionmenu = CTkOptionMenu(master, **properties)
        self.newoptionmenu.place(x=50,y=50)
        self.newoptionmenu.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newoptionmenu = CTkOptionMenu(self.canvas_frame, **properties)
        self.newoptionmenu.place(x=50,y=50)
    self.newoptionmenu.bind("<Button-1>",lambda e,widget=self.newoptionmenu:self.s_drag(e,widget))
    self.newoptionmenu.bind("<B1-Motion>",lambda e,widget=self.newoptionmenu:self.m_drag(e,widget))
    self.newoptionmenu.bind("<ButtonRelease-1>",lambda e,widget=self.newoptionmenu:self.r_drag(e,widget))
    self.newoptionmenu.bind("<Double-Button-1>",lambda e,widget=self.newoptionmenu:self.apply(e,widget))
    self.newoptionmenu.bind("<Button-3>", lambda e,widget=self.newoptionmenu:self.show_properties_menu(e,widget))
    

  def addprogressbar(self,properties=None,master=None):
    if properties==None:
      self.newprogressbar=CTkProgressBar(self.canvas_frame,fg_color="black",progress_color=self.sidebar_button_color,border_color="white",border_width=0)
      self.newprogressbar.place(x=50,y=50)
    else:
      if master!=None:
        self.newprogressbar = CTkProgressBar(master, **properties)
        self.newprogressbar.place(x=50,y=50)
        self.newprogressbar.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newprogressbar = CTkProgressBar(self.canvas_frame, **properties)
        self.newprogressbar.place(x=50,y=50)
    self.newprogressbar.bind("<Button-1>",lambda e,widget=self.newprogressbar:self.s_drag(e,widget))
    self.newprogressbar.bind("<B1-Motion>",lambda e,widget=self.newprogressbar:self.m_drag(e,widget))
    self.newprogressbar.bind("<ButtonRelease-1>",lambda e,widget=self.newprogressbar:self.r_drag(e,widget))
    self.newprogressbar.bind("<Double-Button-1>",lambda e,widget=self.newprogressbar:self.apply(e,widget))
    self.newprogressbar.bind("<Button-3>", lambda e,widget=self.newprogressbar:self.show_properties_menu(e,widget))

  def addradiobutton(self,properties=None,master=None):
    if properties==None:
      self.newradiobutton=CTkRadioButton(self.canvas_frame,fg_color="black",text="Option1",text_color="white",hover_color="gray",border_color="white")
      self.newradiobutton.place(x=50,y=50)
    else:
      if master!=None:
        self.newradiobutton = CTkRadioButton(master, **properties)
        self.newradiobutton.place(x=50,y=50)
        self.newradiobutton.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.newradiobutton = CTkRadioButton(self.canvas_frame, **properties)
        self.newradiobutton.place(x=50,y=50)
    self.newradiobutton.bind("<Button-1>",lambda e,widget=self.newradiobutton:self.s_drag(e,widget))
    self.newradiobutton.bind("<B1-Motion>",lambda e,widget=self.newradiobutton:self.m_drag(e,widget))
    self.newradiobutton.bind("<ButtonRelease-1>",lambda e,widget=self.newradiobutton:self.r_drag(e,widget))
    self.newradiobutton.bind("<Double-Button-1>",lambda e,widget=self.newradiobutton:self.apply(e,widget))
    self.newradiobutton.bind("<Button-3>", lambda e,widget=self.newradiobutton:self.show_properties_menu(e,widget))


  def addframe(self,properties=None,master=None):
    if properties==None:
      self.container=CTkFrame(self.canvas_frame,fg_color="white",border_color="white")
      self.container.place(x=10,y=10)
    else:
      if master!=None:
        self.container = CTkFrame(master, **properties)
        self.container.place(x=50,y=50)
        self.container.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.container = CTkFrame(self.canvas_frame, **properties)
        self.container.place(x=50,y=50)
    self.container.bind("<Button-1>",lambda e,widget=self.container:self.s_drag(e,widget))
    self.container.bind("<B1-Motion>",lambda e,widget=self.container:self.m_drag(e,widget))
    self.container.bind("<ButtonRelease-1>",lambda e,widget=self.container:self.r_drag(e,widget))
    self.container.bind("<Double-Button-1>",lambda e,widget=self.container:self.apply(e,widget))
    self.container.bind("<Button-3>", lambda e,widget=self.container:self.show_properties_menu(e,widget))

  def addslider(self,properties=None,master=None):
    if properties==None:
      self.sliderr=CTkSlider(self.canvas_frame,fg_color="white",progress_color="blue")
      self.sliderr.place(x=10,y=10)
    else:
      if master!=None:
        self.sliderr = CTkSlider(master, **properties)
        self.sliderr.place(x=50,y=50)
        self.sliderr.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.sliderr = CTkSlider(self.canvas_frame, **properties)
        self.sliderr.place(x=50,y=50)
    self.sliderr.bind("<Button-1>",lambda e,widget=self.sliderr:self.s_drag(e,widget))
    self.sliderr.bind("<B1-Motion>",lambda e,widget=self.sliderr:self.m_drag(e,widget))
    self.sliderr.bind("<ButtonRelease-1>",lambda e,widget=self.sliderr:self.r_drag(e,widget))
    self.sliderr.bind("<Double-Button-1>",lambda e,widget=self.sliderr:self.apply(e,widget))
    self.sliderr.bind("<Button-3>", lambda e,widget=self.sliderr:self.show_properties_menu(e,widget))
  
  def addswitch(self,properties=None,master=None):
    if properties==None:
      self.switch=CTkSwitch(self.canvas_frame,fg_color="white",progress_color="blue",text_color="white")
      self.switch.place(x=10,y=10)
    else:
      if master!=None:
        self.switch = CTkSwitch(master, **properties)
        self.switch.place(x=50,y=50)
        self.switch.configure(bg_color="transparent")
        self.delete_widget()
      else:
        self.switch = CTkSwitch(self.canvas_frame, **properties)
        self.switch.place(x=50,y=50)
    self.switch.bind("<Button-1>",lambda e,widget=self.switch:self.s_drag(e,widget))
    self.switch.bind("<B1-Motion>",lambda e,widget=self.switch:self.m_drag(e,widget))
    self.switch.bind("<ButtonRelease-1>",lambda e,widget=self.switch:self.r_drag(e,widget))
    self.switch.bind("<Double-Button-1>",lambda e,widget=self.switch:self.apply(e,widget))
    self.switch.bind("<Button-3>", lambda e,widget=self.switch:self.show_properties_menu(e,widget))
#LeftClick
  def test(self,e,widget):
    print("Hi")

  def s_drag(self,e,widget):
    widget.start_xpos=e.x
    widget.start_ypos=e.y
    self.currenton_widget=widget
    # print(type(widget).__name__)
    if type(self.currenton_widget)==CTkComboBox:
      self.currenton_widget.configure(border_width=0)

    
    
  def m_drag(self,e,widget):
    x=widget.winfo_x()-widget.start_xpos+e.x
    y=widget.winfo_y()-widget.start_ypos+e.y
    
    #Magnet
    if self.magnet.get()==1:
      magnet_spacing = self.magnetnum.get()
      x = round(x / magnet_spacing) * magnet_spacing
      y = round(y / magnet_spacing) * magnet_spacing

    

    widget.place(x=x,y=y)
  def r_drag(self,e,widget):
    self.entry3.configure(state="normal")
    self.entry3.delete(0,END)
    try:
      self.entry3.insert(0,widget.cget("text"))
    except:
      self.entry3.insert(0,type(widget).__name__)
    self.entry3.configure(state="disable")
  def apply(self,e,widget):
    if len(self.entry1.get()) != 0:
      widget.configure(text=self.entry1.get())
      self.entry1.delete(0,END)
    

  def show_canvas_properties_menu(self,e):
    self.properties_menu = tk.Menu(self.window, tearoff=0)
    self.properties_menu.add_command(label="Properties",command=self.show_properties)
    self.properties_menu.add_command(label="Paste",command=self.paste)
    self.properties_menu.add_command(label="Color Finder",command=colorpicker.pickcolor)
    self.properties_menu.add_separator()
    self.properties_menu.tk_popup(e.x_root, e.y_root)
    
  def show_properties_menu(self,e,widget):
    self.entry3.configure(state="normal")
    self.entry3.delete(0,END)
    try:
      self.entry3.insert(0,widget.cget("text"))
    except:
      self.entry3.insert(0,type(widget).__name__)
    self.entry3.configure(state="disable")
    if len(self.entry1.get()) != 0:
      widget.configure(text=self.entry1.get())
      self.entry1.delete(0,END)
    self.currenton_widget=widget
    self.properties_menu = tk.Menu(self.window, tearoff=0)
    self.properties_menu.add_command(label="Properties",command=self.show_properties)
    self.properties_menu.add_command(label="Copy",command=self.copy)
    self.properties_menu.add_command(label="Apply",command=lambda e=None,widget=self.currenton_widget:self.apply(e,widget))
    self.properties_menu.add_command(label="Lock",command=self.lock)
    self.properties_menu.add_command(label="Unlock",command=self.unlock)
    self.properties_menu.add_separator()

    self.properties_menu.add_command(label="Delete",command=self.delete_widget)
    self.properties_menu.tk_popup(e.x_root, e.y_root)

  def lock(self,_=None):
    self.currenton_widget.unbind("<Button-1>")
    self.currenton_widget.unbind("<B1-Motion>")
    self.currenton_widget.unbind("<ButtonRelease-1>")

  def unlock(self,_=None):
    self.currenton_widget.bind("<Button-1>",lambda e,widget=self.currenton_widget:self.s_drag(e,widget))
    self.currenton_widget.bind("<B1-Motion>",lambda e,widget=self.currenton_widget:self.m_drag(e,widget))
    self.currenton_widget.bind("<ButtonRelease-1>",lambda e,widget=self.currenton_widget:self.r_drag(e,widget))

  def copy(self,_=None):
    self.clipboard=self.currenton_widget
    
  def paste(self,e=None,master=None):
    widget_class=type(self.clipboard)
    properties_list=["text","text_color","fg_color","bg_color","hover_color","corner_radius",
                     "font","border_width","border_color","width","height","checkbox_width",
                     "checkbox_height","values","progress_color"]
    properties={
    }
    for k in properties_list:
      try:
        properties[k]=self.clipboard.cget(k)
      except:
        {}
    if widget_class==CTkButton:
      self.addbutton(properties,master=master)
    elif widget_class==CTkLabel:
      self.addlabel(properties,master=master)
    elif widget_class==CTkCheckBox:
      self.addcheckbox(properties,master=master)
    elif widget_class==CTkComboBox:
      self.addcombobox(properties,master=master)
    elif widget_class==CTkEntry:
      self.addentry(properties,master=master)
    elif widget_class==CTkOptionMenu:
      self.addoptionmenu(properties,master=master)
    elif widget_class==CTkProgressBar:
      self.addprogressbar(properties,master=master)
    elif widget_class==CTkFrame:
      self.addframe(properties,master=master)
    elif widget_class==CTkSwitch:
      self.addswitch(properties,master=master)
    elif widget_class==CTkSlider:
      self.addslider(properties,master=master)
    elif widget_class==CTkRadioButton:
      self.addradiobutton(properties,master=master)
  def delete_widget(self,_=None):
    if self.currenton_widget != None:
      self.currenton_widget.destroy()

  def show_properties(self):
    self.properties_window = CTkToplevel(self.window)
    self.properties_window.attributes("-topmost",True)
    self.properties_window.geometry("700x550")
    self.properties_window.title("Properties")

    self.widget_color_label=CTkLabel(self.properties_window,text="Widget Color:")
    self.widget_color_label.grid(row=1,column=0,padx=10,pady=10)
    try:
      if type(self.currenton_widget.cget("fg_color"))==str:
        self.widget_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applywidgetcolor)
        self.widget_color.set(self.currenton_widget.cget("fg_color").capitalize())
        self.widget_color.grid(row=1,column=1,pady=10,padx=10)
      else:
        self.widget_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applywidgetcolor)
        self.widget_color.set("Default")
        self.widget_color.grid(row=1,column=1,pady=10,padx=10)
    except:
      print("Not Here")
      print(self.currenton_widget.cget("fg_color"))
      self.widget_color=CTkLabel(self.properties_window,text="Disabled")
      self.widget_color.grid(row=1,column=1,padx=10,pady=10)
    try:
      self.currenton_widget.cget("text")
      self.widget_text=CTkLabel(self.properties_window,text="Text:")
      self.widget_text.grid(row=0,column=0,pady=10,padx=10)
      self.widget_text_entry=CTkEntry(self.properties_window)
      self.widget_text_entry.grid(row=0,column=1)
      self.widget_text_entry.insert(0,self.currenton_widget.cget("text"))
      self.widget_text_entry.bind("<FocusIn>",lambda e:self.widget_text_entry.delete(0,END))
      self.widget_text_entry.bind("<Return>",self.apply_widget_text)
    except:{}

    self.text_color_label=CTkLabel(self.properties_window,text="Text Color:")
    self.text_color_label.grid(row=2,column=0,padx=10,pady=10)
    try:
      self.text_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applytextcolor)
      self.text_color.set(self.currenton_widget.cget("text_color").capitalize())
      self.text_color.grid(row=2,column=1,pady=10,padx=10)
    except:
      self.text_color=CTkLabel(self.properties_window,text="Disabled")
      self.text_color.grid(row=2,column=1,padx=10,pady=10)

    self.hovered_color_label=CTkLabel(self.properties_window,text="Hovered Color:")
    self.hovered_color_label.grid(row=3,column=0,padx=10,pady=10)
    try:
      if type(self.currenton_widget.cget("hover_color"))==str:
        self.hovered_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applyhovercolor)
        self.hovered_color.set(self.currenton_widget.cget("hover_color").capitalize())
        self.hovered_color.grid(row=3,column=1,pady=10,padx=10)
      elif type(self.currenton_widget.cget("hover_color"))==list:
        self.hovered_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applyhovercolor)
        self.hovered_color.set("Default")
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
    try:

      font = self.currenton_widget.cget("font")
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
      self.font_style=CTkComboBox(self.properties_window,values=["Normal","Bold","Italic","Underline"],command=self.changefont)
      self.font_style.set(font.cget("weight").capitalize())
      self.font_style.grid(row=5,column=5,padx=10,pady=10)
    except:{}

    self.bg_color_lable=CTkLabel(self.properties_window,text="Background Color:")
    self.bg_color_lable.grid(row=6,column=0,padx=10,pady=10)
    try:
      self.bg_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applybgcolor)
      self.bg_color.set("Transparent")
      self.bg_color.grid(row=6,column=1,pady=10,padx=10)
    except:
      self.bg_color=CTkLabel(self.properties_window,text="Transparent")
      self.bg_color.grid(row=6,column=1,padx=10,pady=10)

    self.border_width_label=CTkLabel(self.properties_window,text="Border Thickness")
    self.border_width_label.grid(row=7,column=0,padx=10,pady=10)

    try:
      self.border_width = CTkSlider(self.properties_window, from_=0, to=25, width=150,command=self.applyborderwidth)
      self.border_width.grid(row=7, column=1, padx=10, pady=10)
      self.border_width.set(self.currenton_widget.cget("border_width"))
      
    except:
      self.border_width=CTkLabel(self.properties_window,text="Disabled")
      self.border_width.grid(row=7,column=1,padx=0,pady=10)

    self.border_color_label=CTkLabel(self.properties_window,text="Border Color")
    self.border_color_label.grid(row=8,column=0,padx=10,pady=10)
    try:
      self.border_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applybordercolor)
      self.border_color.set("Transparent")
      self.border_color.grid(row=8,column=1,pady=10,padx=10)
    except:
      self.border_color=CTkLabel(self.properties_window,text="Transparent")
      self.border_color.grid(row=8,column=1,padx=10,pady=10)
    if type(self.currenton_widget)==CTkComboBox or type(self.currenton_widget)==CTkOptionMenu:
      self.addvalue_lable=CTkLabel(self.properties_window,text="Add Value:")
      self.addvalue_lable.grid(row=9,column=0,padx=10,pady=10)
      self.addvalue_entry=CTkEntry(self.properties_window,text_color="gray")
      self.addvalue_entry.insert(0, "Value:")
      self.addvalue_entry.grid(row=9,column=1,pady=10,padx=10)
      self.addvalue_entry.bind("<FocusIn>",lambda e:self.addvalue_entry.delete(0,END))
      self.applyaddvalue_combo=CTkButton(self.properties_window,text="Apply",command=self.applyvalue_combo,width=50)
      self.applyaddvalue_combo.grid(row=9,column=2,pady=10,padx=10)

      self.deletevalue_lable=CTkLabel(self.properties_window,text="Delete Value:")
      self.deletevalue_lable.grid(row=10,column=0,padx=10,pady=10)
      self.deletevalue_box=CTkComboBox(self.properties_window,values=self.currenton_widget.cget("values"),command=self.deletevalue_combo)
      self.deletevalue_box.set("Select")
      self.deletevalue_box.grid(row=10,column=1,pady=10,padx=10)
    if type(self.currenton_widget)==CTkProgressBar or type(self.currenton_widget)==CTkSlider or type(self.currenton_widget)==CTkSwitch:
      self.color_label=CTkLabel(self.properties_window,text="Progress Color:")
      self.color_label.grid(row=9,column=0,padx=10,pady=10)
      self.progrees_color=CTkComboBox(self.properties_window,values=["Gray","White","Black","Blue","Red","Green","Yellow","Purple","Pink","---------------------","Transparent","Custom"],command=self.applyprogresscolor)
      self.progrees_color.set("Pick Color")
      self.progrees_color.grid(row=9,column=1,padx=10,pady=10)


    #Export Issue

    # self.allmaster=[]
    # self.showmaster=[]
    # canvaframe=self.canvas_frame.winfo_children()

    # for i in canvaframe:
    #   if isinstance(i,CTkFrame):
    #     self.allmaster.append(i)
    #     self.showmaster.append(str(len(self.showmaster)+1))
        
    # print(self.allmaster)
    # print(self.showmaster)
    # self.color_label=CTkLabel(self.properties_window,text="Master:")
    # self.color_label.grid(row=10,column=0,padx=10,pady=10)
    # self.progrees_color=CTkComboBox(self.properties_window,values=self.showmaster,command=self.changemaster)
    # self.progrees_color.set("Pick Master")
    # self.progrees_color.grid(row=10,column=1,padx=10,pady=10)

  # def changemaster(self,e):
  #   e=int(e)
  #   self.clipboard=self.currenton_widget
  #   self.paste(master=self.allmaster[e-1])

  def applyprogresscolor(self,v):
    if v=="Custom":
      self.custom_progress_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_progress_color.insert(0, "Hex Color Code:")
      self.custom_progress_color.grid(row=9,column=2,pady=10,padx=10)
      self.custom_progress_color.bind("<FocusIn>",lambda e:self.custom_progress_color.delete(0,END))
      self.applycustom_progress_color_button=CTkButton(self.properties_window,text="Apply",command=self.applycustom_progress_color)
      self.applycustom_progress_color_button.grid(row=9,column=3,pady=10,padx=10)
    else:
      try:
        self.applycustom_progress_color_button.destroy()
        self.custom_progress_color.destroy()
      except:
        {}
      color=v.lower()
      self.currenton_widget.configure(progress_color=color)
  def applycustom_progress_color(self):
    self.currenton_widget.configure(progress_color=self.custom_progress_color.get())

  def applyvalue_combo(self):
    if self.addvalue_entry.get()!="" and self.addvalue_entry.get()!="Value:":
      val=self.currenton_widget.cget("values")
      val.append(self.addvalue_entry.get())
      self.currenton_widget.configure(values=val)
      self.deletevalue_box.configure(values=val)
      self.addvalue_entry.delete(0,END)

  def deletevalue_combo(self,v):
    val=self.currenton_widget.cget("values")
    val.remove(v)
    self.currenton_widget.configure(values=val)
    self.deletevalue_box.configure(values=val)
    self.addvalue_entry.delete(0,END)
    self.deletevalue_box.set("Completed!")



  def applybordercolor(self,v):
    if v=="Custom":
      self.custom_border_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_border_color.insert(0, "Hex Color Code:")
      self.custom_border_color.grid(row=8,column=2,pady=10,padx=10)
      self.custom_border_color.bind("<FocusIn>",lambda e:self.custom_border_color.delete(0,END))
      self.applycustom_border_color_button=CTkButton(self.properties_window,text="Apply",command=self.applycustom_border_color)
      self.applycustom_border_color_button.grid(row=8,column=3,pady=10,padx=10)
    else:
      try:
        self.applycustom_border_color_button.destroy()
        self.custom_border_color.destroy()
      except:
        {}
      
      color=v.lower()
      print(color)
      self.currenton_widget.configure(border_color=color)
  def applycustom_border_color(self):
    self.currenton_widget.configure(border_color=self.custom_border_color.get())

  def applyborderwidth(self,v):
    self.currenton_widget.configure(border_width=self.border_width.get())
  def applybgcolor(self,v):
    if v=="Custom":
      self.custom_bg_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_bg_color.insert(0, "Hex Color Code:")
      self.custom_bg_color.grid(row=6,column=2,pady=10,padx=10)
      self.custom_bg_color.bind("<FocusIn>",lambda e:self.custom_bg_color.delete(0,END))
      self.applycustom_bg_color_button=CTkButton(self.properties_window,text="Apply",command=self.applycustom_bg_color)
      self.applycustom_bg_color_button.grid(row=6,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_bg_color.destroy()
        self.applycustom_bg_color_button.destroy()
      except:
        {}
      
      color=self.bg_color.get().lower()
      print(color)
      self.currenton_widget.configure(bg_color=color)
  def applycustom_bg_color(self):
    self.currenton_widget.configure(bg_color=self.custom_bg_color.get())

  def changefont(self,v):
    
    if self.font_style.get().lower()!="normal":
      # print(f"V:{v}")
      if self.font_style.get()=="Bold":
        currentfont=CTkFont(family=self.font.get(),size=int(self.font_size.get()),weight=self.font_style.get().lower())
        self.currenton_widget.configure(font=currentfont)
      elif self.font_style.get()=="Italic":
        currentfont=CTkFont(family=self.font.get(),size=int(self.font_size.get()),slant=self.font_style.get().lower())
        self.currenton_widget.configure(font=currentfont)
      elif self.font_style.get()=="Underline":
        currentfont=CTkFont(family=self.font.get(),size=int(self.font_size.get()),underline=True)
        self.currenton_widget.configure(font=currentfont)
    else:
      currentfont=CTkFont(family=self.font.get(),size=int(self.font_size.get()))
      self.currenton_widget.configure(font=(currentfont))
    font = self.currenton_widget.cget("font")
    size = font.cget("size")
    family = font.cget("family")
    # print(family)
  def applycornerradius(self,v):
    self.currenton_widget.configure(corner_radius=v)

  def apply_widget_text2(self,e):
    self.currenton_widget.configure(text=self.entry1.get())
  def apply_widget_text(self,e):
    self.currenton_widget.configure(text=self.widget_text_entry.get())
  def applywidgetcolor(self,v):
    if v=="Custom":
      self.custom_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_color.insert(0, "Hex Color Code:")

      self.custom_color.grid(row=1,column=2,pady=10,padx=10)
      self.custom_color.bind("<FocusIn>",lambda e:self.custom_color.delete(0,END))
      self.applycustomcolor=CTkButton(self.properties_window,text="Apply",command=self.apply_widget_custom_color)
      self.applycustomcolor.grid(row=1,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_color.destroy()
        self.applycustomcolor.destroy()
      except:
        {}
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
      self.applycustom_text_color_button=CTkButton(self.properties_window,text="Apply",command=self.applycustom_text_color)
      self.applycustom_text_color_button.grid(row=2,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_text_color.destroy()
        self.applycustom_text_color_button.destroy()
      except:
       {}
      color=self.text_color.get().lower()
      self.currenton_widget.configure(text_color=color)
    

  def applyhovercolor(self,v):
    if v=="Custom":
      self.custom_hovered_color=CTkEntry(self.properties_window,text_color="gray")
      self.custom_hovered_color.insert(0, "Hex Color Code:")
      self.custom_hovered_color.grid(row=3,column=2,pady=10,padx=10)
      self.custom_hovered_color.bind("<FocusIn>",lambda e:self.custom_hovered_color.delete(0,END))
      self.applycustom_hovered_color_button=CTkButton(self.properties_window,text="Apply",command=self.applycustom_hover_color)
      self.applycustom_hovered_color_button.grid(row=3,column=3,pady=10,padx=10)
    else:
      try:
        self.custom_hovered_color.destroy()
        self.applycustom_hovered_color_button.destroy()
      except:
        {}
      color=self.hovered_color.get().lower()
      self.currenton_widget.configure(hover_color=color)

  def applycustom_hover_color(self):
    self.currenton_widget.configure(hover_color=self.custom_hovered_color.get())

set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = GeneratorPage(window)
window.mainloop()