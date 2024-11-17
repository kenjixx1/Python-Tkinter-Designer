from customtkinter import *
from tkinter import filedialog

class ExportPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Export Page")

        # Frame for export options
        self.frame = CTkFrame(self.master)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Label and Entry for file name
        self.label = CTkLabel(self.frame, text="File Name:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        self.file_name_entry = CTkEntry(self.frame, placeholder_text="Enter file name")
        self.file_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Export Button
        self.export_button = CTkButton(self.frame, text="Export", command=self.export_file)
        self.export_button.grid(row=1, column=0, columnspan=2, pady=20)

    def export_file(self):
        # Get the entered file name
        file_name = self.file_name_entry.get()
        if not file_name:
            CTkLabel(self.frame, text="Please enter a file name!", text_color="red").grid(row=2, column=0, columnspan=2)
            return

        # Open save file dialog
        file_path = filedialog.asksaveasfilename(
            title="Select Export Location",
            initialfile=file_name,
            defaultextension=".py",
            filetypes=(("Python Files", "*.py"), ("All Files", "*.*"))
        )

        if file_path:  # If a path is selected
            self.save_file(file_path)

    def save_file(self, file_path):
        # Simulate saving file (replace this with your export logic)
        with open(file_path, "w") as file:
            file.write("# Exported content goes here\n")
            file.write("print('Hello, World!')\n")

        CTkLabel(self.frame, text=f"File saved to {file_path}", text_color="green").grid(row=3, column=0, columnspan=2)

# Main Application
if __name__ == "__main__":
    root = CTk()
    app = ExportPage(root)
    root.mainloop()
