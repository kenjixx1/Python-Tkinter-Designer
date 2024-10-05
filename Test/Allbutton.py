from customtkinter import *

class GeneratorPage:
    def __init__(self, window):
        self.window = window
        self.window.title("Gui Generator")
        self.window.geometry("1800x1080")
        self.window.resizable(True, True)

        # Top Frame
        self.top_frame = CTkFrame(self.window, fg_color="transparent", corner_radius=15, height=100)
        self.top_frame.pack(fill="x", pady=10)

        # Sidebar Frame
        self.sidebar_frame = CTkFrame(self.window, width=200, corner_radius=15, fg_color="#5ce1e6")
        self.sidebar_frame.pack(side="left", fill="y", padx=20, pady=10)

        # Canvas Frame for New Buttons
        self.canvas_frame = CTkFrame(self.window, fg_color="white")
        self.canvas_frame.pack(side="right", fill="both", expand=True, padx=20, pady=10)

        # Menu Frame
        self.menu_frame = CTkFrame(self.top_frame, fg_color="transparent")
        self.tool_frame = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)

        self.widget_button_page1()
        self.menu()
        self.tool()
        self.slider()

    def slider(self):
        # Width Slider
        self.slider_frame = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
        self.slider_frame.grid(row=0, column=2, padx=10, pady=10)

        self.sliderw = CTkSlider(self.slider_frame, from_=1, to=100, width=300, command=self.get_sliderxvalue)
        self.sliderw.grid(row=0, column=0, padx=10, pady=10)
        self.widthlabel = CTkLabel(self.slider_frame, text=f"Width: {int(self.sliderw.get())}", text_color="black", bg_color="transparent")
        self.widthlabel.grid(row=0, column=1, padx=10)

        # Length Slider
        self.slider_framel = CTkFrame(self.top_frame, fg_color="#5ce1e6", corner_radius=15, height=100)
        self.slider_framel.grid(row=0, column=3, padx=10, pady=10)

        self.sliderl = CTkSlider(self.slider_framel, from_=1, to=100, width=300, command=self.get_slideryvalue)
        self.sliderl.grid(row=0, column=0, padx=10, pady=10)
        self.lengthlabel = CTkLabel(self.slider_framel, text=f"Length: {int(self.sliderl.get())}", text_color="black", bg_color="transparent")
        self.lengthlabel.grid(row=0, column=1, padx=10)

        # Segmented Button
        self.segmentedbuttonframe = CTkFrame(self.top_frame, fg_color="transparent", corner_radius=15, height=100)
        self.segmentedbuttonframe.grid(row=1, column=0, padx=10)

        self.sbutton = CTkSegmentedButton(self.segmentedbuttonframe, values=["Design", "Code"], dynamic_resizing=True, height=30, corner_radius=20)
        self.sbutton.set("Design")
        self.sbutton.pack(pady=0, padx=10)

    def get_sliderxvalue(self, x):
        self.widthlabel.configure(text=f"Width: {int(x)}")

    def get_slideryvalue(self, x):
        self.lengthlabel.configure(text=f"Length: {int(x)}")

    def menu(self):
        # Export Button
        self.export_button = CTkButton(self.menu_frame, text="Export", corner_radius=25, width=5, fg_color="#0097b2", command=self.export_action)
        self.export_button.grid(row=0, column=0, padx=5, pady=5)

        # New Button
        self.make_new_button = CTkButton(self.menu_frame, text="New", corner_radius=25, width=5, fg_color="#5ca16c", command=self.new_action)
        self.make_new_button.grid(row=0, column=1, padx=5, pady=5)

        # Save Button
        self.save_button = CTkButton(self.menu_frame, text="Save", corner_radius=25, width=5, fg_color="#ffbe5c", command=self.save_action)
        self.save_button.grid(row=0, column=2, padx=5, pady=5)

        self.menu_frame.grid(row=0, column=0)

    def export_action(self):
        print("Export button clicked!")

    def new_action(self):
        print("New button clicked!")

    def save_action(self):
        print("Save button clicked!")

    def tool(self):
        self.text = CTkLabel(self.tool_frame, text="Text:", fg_color="transparent", text_color="black")
        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry1 = CTkEntry(self.tool_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry1.grid(row=0, column=2, padx=5, pady=5)

        self.text2 = CTkLabel(self.tool_frame, text="Command:", fg_color="transparent", text_color="black")
        self.text2.grid(row=0, column=3, padx=5, pady=5)
        self.entry2 = CTkEntry(self.tool_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry2.grid(row=0, column=4, padx=5, pady=5)

        self.text3 = CTkLabel(self.tool_frame, text="Currently On:", fg_color="transparent", text_color="black")
        self.text3.grid(row=0, column=6, padx=5, pady=5)
        self.entry3 = CTkEntry(self.tool_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry3.grid(row=0, column=7, padx=5, pady=5)

        self.tool_frame.grid(row=0, column=1, padx=10, pady=10)

    def widget_button_page1(self):
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, text="Frame", corner_radius=15, height=50, command=lambda: self.add_frame_button("Custom Frame"))
        self.sidebar_button_1.pack(pady=10, padx=20)

        self.sidebar_button_2 = CTkButton(self.sidebar_frame, text="Label", corner_radius=15, height=50, command=lambda: self.add_label_button("Custom Label"))
        self.sidebar_button_2.pack(pady=10, padx=20)

        self.sidebar_button_3 = CTkButton(self.sidebar_frame, text="Button", corner_radius=15, height=50, command=lambda: self.add_button_button("Custom Button"))
        self.sidebar_button_3.pack(pady=10, padx=20)

        self.sidebar_button_4 = CTkButton(self.sidebar_frame, text="CheckBox", corner_radius=15, height=50, command=lambda: self.add_checkbox_button("Custom CheckBox"))
        self.sidebar_button_4.pack(pady=10, padx=20)

        self.sidebar_button_5 = CTkButton(self.sidebar_frame, text="ComboBox", corner_radius=15, height=50, command=lambda: self.add_combobox_button("Custom ComboBox"))
        self.sidebar_button_5.pack(pady=10, padx=20)

        self.sidebar_button_6 = CTkButton(self.sidebar_frame, text="Entry", corner_radius=15, height=50, command=lambda: self.add_entry_button("Custom Entry"))
        self.sidebar_button_6.pack(pady=10, padx=20)

        self.sidebar_button_7 = CTkButton(self.sidebar_frame, text="OptionMenu", corner_radius=15, height=50, command=lambda: self.add_option_menu_button("Custom Option Menu"))
        self.sidebar_button_7.pack(pady=10, padx=20)

        self.sidebar_button_8 = CTkButton(self.sidebar_frame, text="ProgressBar", corner_radius=15, height=50, command=self.add_progress_bar_button)
        self.sidebar_button_8.pack(pady=10, padx=20)

        self.sidebar_button_9 = CTkButton(self.sidebar_frame, text="RadioButton", corner_radius=15, height=50, command=lambda: self.add_radio_button("Custom RadioButton"))
        self.sidebar_button_9.pack(pady=10, padx=20)

        self.sidebar_button_10 = CTkButton(self.sidebar_frame, text="ScrollableFrame", corner_radius=15, height=50, command=self.add_scrollable_frame_button)
        self.sidebar_button_10.pack(pady=10, padx=20)

        self.sidebar_button_11 = CTkButton(self.sidebar_frame, text="SegmentedButton", corner_radius=15, height=50, command=lambda: self.add_segmented_button("Custom SegmentedButton"))
        self.sidebar_button_11.pack(pady=10, padx=20)

        self.sidebar_button_12 = CTkButton(self.sidebar_frame, text="Slider", corner_radius=15, height=50, command=lambda: self.add_slider_button("Custom Slider"))
        self.sidebar_button_12.pack(pady=10, padx=20)

    def add_frame_button(self, frame_text):
        new_frame = CTkFrame(self.canvas_frame, corner_radius=15, fg_color="#a6a6a6", height=50)
        new_frame.pack(pady=10, padx=10, fill='x')
        CTkLabel(new_frame, text=frame_text, fg_color="transparent").pack()

    def add_label_button(self, label_text):
        new_label = CTkLabel(self.canvas_frame, text=label_text, fg_color="transparent")
        new_label.pack(pady=10, padx=10)

    def add_button_button(self, button_text):
        new_button = CTkButton(self.canvas_frame, text=button_text, corner_radius=15)
        new_button.pack(pady=10, padx=10)

    def add_checkbox_button(self, checkbox_text):
        new_checkbox = CTkCheckBox(self.canvas_frame, text=checkbox_text)
        new_checkbox.pack(pady=10, padx=10)

    def add_combobox_button(self, combobox_text):
        new_combobox = CTkOptionMenu(self.canvas_frame, values=["Option 1", "Option 2", "Option 3"], text_color="black")
        new_combobox.pack(pady=10, padx=10)

    def add_entry_button(self, entry_text):
        new_entry = CTkEntry(self.canvas_frame, fg_color="#a6a6a6", corner_radius=15)
        new_entry.pack(pady=10, padx=10)

    def add_option_menu_button(self, option_menu_text):
        new_option_menu = CTkOptionMenu(self.canvas_frame, values=["Option 1", "Option 2", "Option 3"], text_color="black")
        new_option_menu.pack(pady=10, padx=10)

    def add_progress_bar_button(self):
        new_progress_bar = CTkProgressBar(self.canvas_frame, mode="determinate")
        new_progress_bar.pack(pady=10, padx=10)

    def add_radio_button(self, radio_text):
        new_radio_button = CTkRadioButton(self.canvas_frame, text=radio_text)
        new_radio_button.pack(pady=10, padx=10)

    def add_scrollable_frame_button(self):
        new_scrollable_frame = CTkScrollableFrame(self.canvas_frame, width=200, height=100, corner_radius=15)
        new_scrollable_frame.pack(pady=10, padx=10)
        new_scrollable_frame.pack_propagate(False)

        # Add some content to the scrollable frame
        CTkLabel(new_scrollable_frame, text="Scrollable Frame Content").pack(pady=10, padx=10)

    def add_segmented_button(self, segmented_text):
        new_segmented_button = CTkSegmentedButton(self.canvas_frame, values=["Option 1", "Option 2"], dynamic_resizing=True)
        new_segmented_button.pack(pady=10, padx=10)

    def add_slider_button(self, slider_text):
        new_slider = CTkSlider(self.canvas_frame, from_=1, to=100, width=300)
        new_slider.pack(pady=10, padx=10)

# Run the application
set_appearance_mode("dark")
set_default_color_theme("blue")
window = CTk()
app = GeneratorPage(window)
window.mainloop()
