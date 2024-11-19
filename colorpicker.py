from customtkinter import *
import pyperclip
import time


class ColorPick:
    def __init__(self):
        pass
    def run(self):
        
        
        window=CTk()
        window.geometry("500x500")
        window.title("Color Picker")
        window.resizable(False, False)
        window.configure(fg_color="#fafafa")


        frame = CTkFrame(window, width=500, height=400, fg_color="#fafafa")
        topframe= CTkFrame(frame, width=440, height=200, fg_color="#fafafa")
        bottomframe = CTkFrame(frame, width=440, height=250, fg_color="#ffffff",border_width=1,border_color="#000000")

        topframe.grid_propagate(False)
        bottomframe.grid_propagate(False)

        red=CTkLabel(bottomframe,text="Red",text_color="#000000",fg_color="transparent")
        red.place(x=70, y=15)

        green=CTkLabel(bottomframe,text="Green",text_color="#000000",fg_color="transparent")
        green.place(x=60, y=75)

        blue=CTkLabel(bottomframe,text="Blue",text_color="#000000",fg_color="transparent")
        blue.place(x=70, y=135)

        def copy():
            pyperclip.copy(preview.cget("fg_color"))
            copy_text.configure(text="Color Copied to Clipboard")
            copy_text.after(2000, lambda: copy_text.configure(text=""))
        
        preview=CTkButton(topframe,fg_color="#000000",width=100,height=100,corner_radius=100,text="",command=copy)
        preview.grid(column=1, row=0, padx=180, pady=50)

        def update_color(x,e=None):
            r, g, b = red_slider.get(), green_slider.get(), blue_slider.get()
            hex_color = f"#{int(r):02x}{int(g):02x}{int(b):02x}"
            preview.configure(fg_color=hex_color)
            
            if e !=None:
                e.set(min(r,g,b))

        def bright(x):
            r, g, b = red_slider.get(), green_slider.get(), blue_slider.get()
            track.append(min(r,g,b))
            diff=track[1]-track[0]
            


            
            print(track)
            m=None
            mm=None
            if r==min(r,g,b):
                m=red_slider
                mm=1
            if g==min(r,g,b):
                m=green_slider
                mm=2
            if b==min(r,g,b):
                m=blue_slider
                mm=3

            
            if mm==1:
                green_slider.set(g+diff)
                blue_slider.set(b+diff)
            elif mm==2:
                red_slider.set(r+diff)
                blue_slider.set(b+diff)
            elif mm==3:
                red_slider.set(r+diff)
                green_slider.set(g+diff)
            m.set(brightness_slider.get())
            if len(track)==2:
                track.pop(0)
            update_color(0)


        track=[0]
        brightness_slider=CTkSlider(topframe,from_=0, to=255, fg_color="#e5e5e5",width=255,height=20,command=bright,progress_color="#4086c2")
        brightness_slider.place(x=100, y=180)
        brightness_slider.set(0)

        red_slider=CTkSlider(bottomframe,from_=0, to=255, fg_color="#e5e5e5",width=255,height=20,command=lambda x,e=brightness_slider:update_color(x,e),progress_color="#4086c2")
        red_slider.set(0)
        red_slider.grid(column=1, row=1, padx=100, pady=20)

        green_slider=CTkSlider(bottomframe,from_=0, to=255, fg_color="#e5e5e5",width=255,height=20,command=lambda x,e=brightness_slider:update_color(x,e),progress_color="#4086c2")
        green_slider.set(0)
        green_slider.grid(column=1, row=2, padx=100, pady=20)

        blue_slider=CTkSlider(bottomframe,from_=0, to=255, fg_color="#e5e5e5",width=255,height=20,command=lambda x,e=brightness_slider:update_color(x,e),progress_color="#4086c2")
        blue_slider.set(0)
        blue_slider.grid(column=1, row=3, padx=100, pady=20)

        

        
        textentry=CTkEntry(bottomframe,width=100,placeholder_text="Hex Code")
        textentry.place(x=120, y=180)


        def change_slider():
            hex_code = textentry.get()
            try:
                r, g, b = int(hex_code[1:3], 16), int(hex_code[3:5], 16), int(hex_code[5:7], 16)
                print(r, g, b)
                red_slider.set(r)
                green_slider.set(g)
                blue_slider.set(b)
                brightness_slider.set(min(r,g,b))
                update_color(0)
            except:
                pass
        confirmbutton=CTkButton(bottomframe,text="Confirm",width=70,height=30,fg_color="#0097b2",command=change_slider)
        confirmbutton.place(x=230, y=180)


        copy_text=CTkLabel(bottomframe,text="",text_color="#000000",fg_color="transparent",anchor="center")
        copy_text.place(x=150, y=220)
        
        topframe.grid(column=0, row=0, padx=10, pady=10)
        bottomframe.grid(column=0, row=1, padx=10, pady=10)
        frame.pack()
        window.mainloop()


    


