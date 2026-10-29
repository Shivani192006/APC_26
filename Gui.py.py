import tkinter as tk

# Save data
def submit():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()

    with open("students.txt", "a") as file:
        file.write(name + "," + mobile + "," + email + "\n")

    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# Read data
def read_data():
    page = tk.Toplevel()
    page.title("Student Records")

    # Headings
    tk.Label(page, text="Name", width=15).grid(row=0, column=0)
    tk.Label(page, text="Mobile", width=15).grid(row=0, column=1)
    tk.Label(page, text="Email", width=20).grid(row=0, column=2)

    # Read file
    with open("students.txt", "r") as file:
        records = file.readlines()

    row = 1

    for record in records:
        data = record.strip().split(",")

        tk.Label(page, text=data[0]).grid(row=row, column=0)
        tk.Label(page, text=data[1]).grid(row=row, column=1)
        tk.Label(page, text=data[2]).grid(row=row, column=2)

        row = row + 1


# Main window
window = tk.Tk()
window.title("Student Application")
window.geometry("400x350")

tk.Label(window, text="Student Details",
         font=("Arial", 18)).pack(pady=15)

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Mobile No.").pack()
mobile_entry = tk.Entry(window)
mobile_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window)
email_entry.pack()

tk.Button(window, text="Submit",
          command=submit).pack(pady=15)

tk.Button(window, text="Read",
          command=read_data).pack()

window.mainloop()
