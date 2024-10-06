import customtkinter as ctk
from tkinter import IntVar

class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkCheckBox Example")
        self.geometry("300x200")

        # IntVar to hold checkbox state
        self.checkbox_var = IntVar()

        # Create CTkCheckBox
        self.checkbox = ctk.CTkCheckBox(self, text="Check me!", variable=self.checkbox_var, command=self.on_check)
        self.checkbox.pack(pady=20)
        self.checkbox2 = ctk.CTkCheckBox(self, text="Check me!", variable=self.checkbox_var, command=self.on_check)
        self.checkbox2.pack(pady=20)

        # Button to check the state of the checkbox
        self.button = ctk.CTkButton(self, text="Get CheckBox State", command=self.get_checkbox_state)
        self.button.pack(pady=20)

    def on_check(self):
        if self.checkbox_var.get() == 1:
            print("Checkbox is checked!")
        else:
            print("Checkbox is unchecked!")

    def get_checkbox_state(self):
        state = self.checkbox_var.get()
        print(f"Checkbox State: {state}")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
