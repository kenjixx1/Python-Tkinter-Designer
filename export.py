from customtkinter import *
import tkinter 
from tkinter import filedialog


255



#00 ff 00

def export(frame,path):
    print('Exporting...')
    list_widget_class=[]
    list_properties=[]
    properties_list=["text","text_color","fg_color","bg_color","hover_color","corner_radius",
                     "font","border_width","border_color","width","height","checkbox_width",
                     "checkbox_height","values","progress_color","frame"]
    
    frame_properties_list=["fg_color","bg_color","width","height"]
    frameprop={}
    for k in frame_properties_list:
        try:
            frameprop[k]=frame.cget(k)
        except:
            pass
    
    

    widgets_on_frame = frame.winfo_children()
    filtered_list = [obj for obj in widgets_on_frame if not isinstance(obj, tkinter.Menu)]
    filtered_list = [obj for obj in widgets_on_frame if not isinstance(obj, CTkToplevel)]
    for i in filtered_list:
        print(type(i).__name__)
    # for i in filtered_list:
    #     if type(i).__name__=="Menu":
    #         filtered_list.remove(i)
    # print(filtered_list)
        
    for widget in filtered_list:
        widget_class = type(widget).__name__
        
        list_widget_class.append(widget_class)
        if widget_class != "Menu":
            prop={}
            for k in properties_list:
                if k=="font":
                    try:
                        font = widget.cget("font")
                        size = font.cget("size")
                        family = font.cget("family")
                        weight=font.cget("weight")
                        all_font = f"{family},{size},{weight}"
                        prop[k]=all_font
                    except:
                        pass
                elif k=="frame": 
                    print("Making Frame")
                    print(widget.master)
                    prop[k]=widget.master
                else:
                    try:
                        prop[k]=widget.cget(k)
                    except:
                        pass
            list_properties.append(prop)

    for i in list_widget_class:
        if "Menu" in list_widget_class:
            list_widget_class.remove("Menu")

    
    
    buttonlist=[]
    labellist=[]
    entrylist=[]
    checkbuttonlist=[]
    radiobuttonlist=[]
    progressbarlist=[]
    framelist=[]
    sliderlist=[]
    switchlist=[]
    optionmenulist=[]
    

    with open(path,"w") as f:
        f.write("from customtkinter import *\n")
        f.write("import tkinter as tk\n")
        f.write("\n")

        f.write(f"""window = CTk()\nwindow.geometry("{frameprop["width"]}x{frameprop["height"]}")\nframe = CTkFrame(window,fg_color="{frameprop["fg_color"]}",
                bg_color="{frameprop["bg_color"]}",width={frameprop["width"]},height={frameprop["height"]})\n\nwindow.resizable(False,False)\n\n""")

    
    with open(path,"a") as f:
        for index,dic in enumerate(list_properties):
            name=""
            # print(list_widget_class[index])
            if list_widget_class[index] == "CTkButton":
                buttonlist.append(dic)
                name=f"button{len(buttonlist)}"

            elif list_widget_class[index] == "CTkLabel":
                labellist.append(dic)
                name=f"label{index}"
            
            elif list_widget_class[index] == "CTkEntry":
                entrylist.append(dic)
                name=f"entry{index}"
            
            elif list_widget_class[index] == "CTkCheckBox":
                checkbuttonlist.append(dic)
                name=f"checkbox{index}"
            
            elif list_widget_class[index] == "CTkComboBox":
                radiobuttonlist.append(dic)
                name=f"combobox{index}"
            
            elif list_widget_class[index] == "CTkProgressBar":
                progressbarlist.append(dic)
                name=f"progressbar{index}"
                # print("Here")
            elif list_widget_class[index]=="CTkFrame":
                framelist.append(dic)
                name=f"frame{index}"
            elif list_widget_class[index]=="CTkSlider":
                sliderlist.append(dic)
                name=f"sliderr{index}"
            elif list_widget_class[index]=="CTkSwitch":
                switchlist.append(dic)
                name=f"Swich{index}"
            elif list_widget_class[index]=="CTkOptionMenu":
                optionmenulist.append(dic)
                name=f"OptionMenu{index}"
            elif list_widget_class[index]=="CTkRadioButton":
                radiobuttonlist.append(dic)
                name=f"Radio{index}"
            
            
            f.write(f"{name}={list_widget_class[index]}(frame,")
            for i,(k,v) in enumerate(dic.items()):
                if len(name)>0:
                    if i == len(dic) - 1:
                        if k=="font":
                            family,size=v.split(",")
                            f.write(f'font=CTkFont(family="{family}",size={size},weight="{weight}")')
                        elif k=="values":
                            f.write(f'{k}={v}')
                        elif k=="frame":
                            {}
                        else:
                            try:
                                float(v)
                                f.write(f'{k}={v}')
                            except: 
                                f.write(f'{k}="{v}"')
                    else:
                        if k=="font":
                            family,size,weight=v.split(",")
                            f.write(f'font=CTkFont(family="{family}",size={size},weight="{weight}"),')
                        elif k=="values":
                            f.write(f'{k}={v},')
                        else:
                            try:
                                float(v)
                                f.write(f'{k}={v},')
                            except: 
                                f.write(f'{k}="{v}",')




            f.write(")\n") 
            f.write(f"{name}.place(x={filtered_list[index].winfo_x()},y={filtered_list[index].winfo_y()})\n")
       


    with open(path,"a") as f:
        f.write("""\nframe.pack()\nset_appearance_mode("dark")\nset_default_color_theme("blue") \nwindow.mainloop()""")

