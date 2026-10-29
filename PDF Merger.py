import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger


# Function to merge PDFs
def merge_pdf():
    
    # Select first PDF
    pdf1 = filedialog.askopenfilename(
        title="Select PDF 1",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if pdf1 == "":
        return

    # Select second PDF
    pdf2 = filedialog.askopenfilename(
        title="Select PDF 2",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if pdf2 == "":
        return

    # Select location for merged PDF
    output = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if output == "":
        return

    # Create PDF merger
    merger = PdfMerger()

    # Add PDF 1
    merger.append(pdf1)

    # Add PDF 2
    merger.append(pdf2)

    # Create merged PDF
    merger.write(output)

    # Close merger
    merger.close()

    messagebox.showinfo(
        "Success",
        "PDFs merged successfully!"
    )


# Create window
window = tk.Tk()

window.title("PDF Merge")
window.geometry("400x250")


# Heading
heading = tk.Label(
    window,
    text="PDF Merge",
    font=("Arial", 20)
)

heading.pack(pady=30)


# Merge button
merge_button = tk.Button(
    window,
    text="Select PDFs and Merge",
    font=("Arial", 14),
    command=lambda: merge_pdf()
)

merge_button.pack(pady=30)


# Keep window open
window.mainloop()
