def colorapply(self, v):
    if v == "Custom":
        self.custom_color = CTkEntry(self.color_window)
        self.custom_color.place(relx=0.1, y=50)

        # Correctly bind the focus events
        self.custom_color.bind("<FocusOut>", self.set_entry)
        self.custom_color.bind("<FocusIn>", self.clear_entry)

        self.applycustomcolor = CTkButton(self.color_window, text="Apply To Preview")
        self.applycustomcolor.place(relx=0.1, y=90)

    else:
        # Destroy the widgets if they exist
        try:
            self.custom_color.destroy()
            self.applycustomcolor.destroy()
        except AttributeError:
            print("No Custom Color to destroy")

# Insert placeholder text if the entry is empty
def set_entry(self, event=None):  # Add event argument
    if self.custom_color.get() == "":
        self.custom_color.insert(0, "Hex Color Code:")
        print("Placeholder added")

# Clear the entry when focused
def clear_entry(self, event=None):  # Add event argument
    self.custom_color.delete(0, END)
    print("Entry cleared")
