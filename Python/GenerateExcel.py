import openpyxl
import tkinter as tk
from tkinter import filedialog

def generate_excel_file(filename, data):
    """
    Generates an Excel file with the specified filename and data.

    Args:
        filename (str): The desired name of the Excel file.
        data (list): A list of lists containing the data to be written to the file.
    """

    # Create a new workbook
    workbook = openpyxl.Workbook()

    # Get the active worksheet
    sheet = workbook.active

    # Write the data to the worksheet
    for row_index, row_data in enumerate(data, start=1):
        for col_index, cell_value in enumerate(row_data, start=1):
            sheet.cell(row=row_index, column=col_index).value = cell_value

    # Save the workbook
    workbook.save(filename)

def create_gui():
    """
    Creates a simple GUI for generating Excel files.
    """

    # Create the main window
    window = tk.Tk()
    window.title("Excel File Generator")

    # Create a label for the filename
    filename_label = tk.Label(window, text="Enter the filename:")
    filename_label.pack()

    # Create a text entry for the filename
    filename_entry = tk.Entry(window)
    filename_entry.pack()

    # Create a button to select the filename
    select_file_button = tk.Button(window, text="Select File", command=lambda: select_filename(filename_entry))
    select_file_button.pack()

    # Create a label for the data
    data_label = tk.Label(window, text="Enter the data (as a list of lists):")
    data_label.pack()

    # Create a text entry for the data
    data_entry = tk.Text(window)
    data_entry.pack()

    # Create a button to generate the Excel file
    generate_button = tk.Button(window, text="Generate Excel", command=lambda: generate_file(filename_entry.get(), data_entry.get()))
    generate_button.pack()

    # Start the GUI event loop
    window.mainloop()

def select_filename(filename_entry):
    """
    Opens a file dialog to select the filename.
    """

    filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
    filename_entry.insert(0, filename)

def generate_file(filename, data_text):
    """
    Generates the Excel file with the specified filename and data.
    """

    try:
        data = eval(data_text)  # Evaluate the text as a Python expression
        generate_excel_file(filename, data)
        print(f"Excel file '{filename}' generated successfully!")
    except Exception as e:
        print(f"Error generating Excel file: {e}")

if __name__ == "__main__":
    create_gui()