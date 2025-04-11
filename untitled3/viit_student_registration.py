from tkinter import *

subject_count = 5  # Adjust this based on the number of subjects

window = Tk()
window.title("MARKSHEET")
window.geometry("700x550")


name_label = Label(window, text="Name", font=("Arial", 12))
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(window, width=20)
name_entry.grid(row=0, column=1, sticky=W)

reg_no_label = Label(window, text="Reg.No", font=("Arial", 12))
reg_no_label.grid(row=1, column=0, sticky=W)
reg_no_entry = Entry(window, width=20)
reg_no_entry.grid(row=1, column=1, sticky=W)


sr_no_label = Label(window, text="Sr.No", font=("Arial", 12))
sr_no_label.grid(row=4, column=0, sticky=W)

subject_label = Label(window, text="Subject", font=("Arial", 12))
subject_label.grid(row=4, column=1, sticky=W)

grade_label = Label(window, text="Grade", font=("Arial", 12))
grade_label.grid(row=4, column=2, sticky=W)

sub_credit_label = Label(window, text="Sub Credit", font=("Arial", 12))
sub_credit_label.grid(row=4, column=3, sticky=W)

credit_obtained_label = Label(window, text="Credit Obtained", font=("Arial", 12))
credit_obtained_label.grid(row=4, column=4, sticky=W)


serial_labels = []
for i in range(1, subject_count+1):
    serial_labels.append(Label(window, text=str(i), font=("Arial", 12)))
    serial_labels[i-1].grid(row=5+i-1, column=0, sticky=W)


subject_labels = []
for i in range(subject_count):
    subject_labels.append(Label(window, text=f"Subject {i+1}", font=("Arial", 12)))
    subject_labels[i].grid(row=5+i, column=1, sticky=W)


marks_entry = []
credit_entry = []
for i in range(subject_count):
    marks_entry.append(Entry(window, width=10))
    marks_entry[i].grid(row=5+i, column=2)
    credit_entry.append(Entry(window, width=5))
    credit_entry[i].grid(row=5+i, column=3)


calculate_sgpa_button = Button(window, text="Calculate SGPA")
calculate_sgpa_button.grid(row=subject_count+6, column=0, columnspan=5, pady=10)

sgpa_label = Label(window, text="SGPA: ", font=("Arial", 12))
sgpa_label.grid(row=subject_count+7, column=0, columnspan=5)

btn1 = Button(window, text="Submit", background="Yellow", font="Arial")
btn1.place(x=90, y=250)

window.mainloop()
