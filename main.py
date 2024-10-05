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

    

    
    self.widget_button_page1()
    self.menu()
    self.tool()
    self.slider()
    
  def slider(self):
    self.slider_frame = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
    self.slider_frame.grid(row=0,column=2,padx=10 ,pady=10)
    self.sliderw = CTkSlider(self.slider_frame, from_=1, to=100, width=300,command=self.get_sliderxvalue)
    self.sliderw.grid(row=0, column=6, padx=10, pady=10)
    self.widthlabel=CTkLabel(self.slider_frame,text=f"Width:{int(self.sliderw.get())}",text_color="black",bg_color="transparent")
    self.widthlabel.grid(row=0,column=5,padx=10)


    self.slider_framel = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
    self.slider_framel.grid(row=0,column=3,padx=10 ,pady=10)
    self.sliderl = CTkSlider(self.slider_framel, from_=1, to=100, width=300,command=self.get_slideryvalue)
    self.sliderl.grid(row=0, column=6, padx=10, pady=10)
    self.lenghtlabel=CTkLabel(self.slider_framel,text=f"Length:{int(self.sliderl.get())}",text_color="black",bg_color="transparent")
    self.lenghtlabel.grid(row=0,column=5,padx=10)

    self.segmentedbuttonframe = CTkFrame(self.top_frame, fg_color="transparent", corner_radius=15, height=100)
    self.segmentedbuttonframe.grid(row=1,column=0,padx=10)

    self.sbutton=CTkSegmentedButton(self.segmentedbuttonframe,values=["Design","Code"],dynamic_resizing=True,height=30,corner_radius=20)
    self.sbutton.set("Design")
    self.sbutton.pack(pady=0,padx=10)

  def get_sliderxvalue(self,x):
    self.widthlabel.configure(text=f"Width: {int(x):02d}")
  def get_slideryvalue(self,x):
    self.lenghtlabel.configure(text=f"Width: {int(x):02d}")


  def menu(self):
    self.export_button=CTkButton(self.menu_frame,text="Export",corner_radius=25,width=5,fg_color="#0097b2")
    self.export_button.grid(row=0,column=0,padx=5,pady=5)

    self.make_new_button=CTkButton(self.menu_frame,text="New",corner_radius=25,width=5,fg_color="#5ca16c")
    self.make_new_button.grid(row=0,column=1,padx=5,pady=5)

    self.save_button=CTkButton(self.menu_frame,text="Save",corner_radius=25,width=5,fg_color="#ffbe5c")
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


    self.tool_frame.grid(row=0,column=1,padx=10 ,pady=10)

  def widget_button_page1(self):
    self.sidebar_button_1 = CTkButton(self.sidebar_frame, text="Frame", corner_radius=15,height=50)
    self.sidebar_button_1.pack(pady=10, padx=20)

    self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="Label", corner_radius=15,height=50)
    self.sidebar_button_2.pack(pady=10, padx=20)

    self.sidebar_button_3 = CTkButton(self.sidebar_frame, text="Button", corner_radius=15,height=50)
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



    

  
    

set_appearance_mode("dark")  
set_default_color_theme("blue")  
window = CTk()
app = GeneratorPage(window)
window.mainloop()