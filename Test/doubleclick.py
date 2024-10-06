import customtkinter as ctk

def on_double_click(event):
    print("Double-clicked!")

# Create a CTk window
app = ctk.CTk()

# Create a button or other widget
button = ctk.CTkButton(app, text="Double Click Me")
button.pack(pady=20)

# Bind double-click event to the button
button.bind("<Double-Button-1>", on_double_click)

app.mainloop()
