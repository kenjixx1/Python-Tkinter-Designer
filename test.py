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
        self.canvas_frame = CTkFrame(self.window, fg_color="transparent")
        self.canvas_frame.pack(side="right", fill="both", expand=True, padx=20, pady=10)

        # List to store button references
        self.button_references = []

        # Variable to store the last clicked button
        self.last_clicked_button = None

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
        self.export_button = CTkButton(self.top_frame, text="Export", corner_radius=25, width=5, fg_color="#0097b2", command=self.export_action)
        self.export_button.grid(row=0, column=0, padx=5, pady=5)

        # New Button
        self.make_new_button = CTkButton(self.top_frame, text="New", corner_radius=25, width=5, fg_color="#5ca16c", command=self.new_action)
        self.make_new_button.grid(row=0, column=1, padx=5, pady=5)

        # Save Button
        self.save_button = CTkButton(self.top_frame, text="Save", corner_radius=25, width=5, fg_color="#ffbe5c", command=self.save_action)
        self.save_button.grid(row=0, column=2, padx=5, pady=5)

    def export_action(self):
        print("Export button clicked!")

    def new_action(self):
        # Call a function to create a new button with a name
        self.add_button()

    def save_action(self):
        print("Save button clicked!")

    def tool(self):
        self.text = CTkLabel(self.top_frame, text="Text:", fg_color="transparent", text_color="black")
        self.text.grid(row=0, column=1, padx=5, pady=5)
        self.entry1 = CTkEntry(self.top_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry1.grid(row=0, column=2, padx=5, pady=5)

        self.text2 = CTkLabel(self.top_frame, text="Command:", fg_color="transparent", text_color="black")
        self.text2.grid(row=0, column=3, padx=5, pady=5)
        self.entry2 = CTkEntry(self.top_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry2.grid(row=0, column=4, padx=5, pady=5)

        self.text3 = CTkLabel(self.top_frame, text="Currently On:", fg_color="transparent", text_color="black")
        self.text3.grid(row=0, column=6, padx=5, pady=5)
        self.entry3 = CTkEntry(self.top_frame, fg_color="#a6a6a6", corner_radius=15)
        self.entry3.grid(row=0, column=7, padx=5, pady=5)

    def widget_button_page1(self):
        self.sidebar_button_1 = CTkButton(self.sidebar_frame, text="Add Button", corner_radius=15, height=50, command=self.add_button)
        self.sidebar_button_1.pack(pady=10, padx=20)

    def add_button(self):
        # Get the name for the new button from the entry field
        button_name = self.entry1.get() if self.entry1.get() else "Dynamic Button"
        
        # Create a new button and store its reference
        new_button = CTkButton(self.canvas_frame, text=button_name, corner_radius=15, command=lambda: self.change_button_properties(new_button))
        new_button.pack(pady=10, padx=10)

        # Store the reference in the list
        self.button_references.append(new_button)

    def change_button_properties(self, button):
        # Change properties of the specific button clicked
        button.configure(text="Clicked!", fg_color="#ff5c5c")

        # Update the "Currently On" entry with the clicked button's text
        self.entry3.delete(0, END)  # Clear the current entry
        self.entry3.insert(0, button.cget("text"))  # Set it to the clicked button's text

# Run the application
set_appearance_mode("dark")
set_default_color_theme("blue")
window = CTk()
app = GeneratorPage(window)
window.mainloop()
