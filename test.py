import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Retrieve Font Example")

        # Create a button with a custom font
        custom_font = ctk.CTkFont(family="Helvetica", size=18, weight="bold")
        self.button = ctk.CTkButton(self, text="Button", font=custom_font)
        self.button.place(x=100, y=100)

        # Fetch the font information
        self.fetch_font_info(self.button)

    def fetch_font_info(self, widget):
        # Get the CTkFont object from the widget
        font_obj = widget.cget("font")
        
        if isinstance(font_obj, ctk.CTkFont):
            # Extract font family, size, and other properties
            font_family = font_obj.cget("family")
            font_size = font_obj.cget("size")
            font_weight = font_obj.cget("weight")
            font_slant = font_obj.cget("slant")

            print(f"Font Family: {font_family}")
            print(f"Font Size: {font_size}")
            print(f"Font Weight: {font_weight}")
            print(f"Font Slant: {font_slant}")

        else:
            print("No valid CTkFont found for the widget.")

# Run the application
app = App()
app.mainloop()
