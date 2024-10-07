import customtkinter as ctk

# Initialize CTk window
root = ctk.CTk()
root.geometry("400x300")
root.title("CTk ComboBox Append Example")

# Function to show the selected option
def show_selected():
    selected_option = combobox.get()
    label.config(text=f"Selected: {selected_option}")

# Function to append a new value to the ComboBox
def append_value():
    new_value = entry.get()
    if new_value:  # If there's text in the entry
        # Get current values from the ComboBox
        current_values = list(combobox.cget("values"))
        if new_value not in current_values:  # Avoid duplicate entries
            current_values.append(new_value)
            combobox.configure(values=current_values)  # Update ComboBox with new values
        entry.delete(0, ctk.END)  # Clear the entry field

# Create a ComboBox with no predefined values
combobox = ctk.CTkComboBox(root, values=[])
combobox.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

# Create a button to show the selected option
button_show = ctk.CTkButton(root, text="Show Selected", command=show_selected)
button_show.place(relx=0.5, rely=0.35, anchor=ctk.CENTER)

# Create a label to display the selected option
label = ctk.CTkLabel(root, text="Selected: None")
label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Entry to input new value
entry = ctk.CTkEntry(root, placeholder_text="New value")
entry.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)

# Create a button to append the new value to the ComboBox
button_append = ctk.CTkButton(root, text="Append Value", command=append_value)
button_append.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

# Start the CTk window
root.mainloop()
