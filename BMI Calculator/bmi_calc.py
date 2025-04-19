from tkinter import *
from tkinter import messagebox

def calc():
    try:
        age = int(age_entry.get())
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / ((height / 100) ** 2)

        if 1 <= age <= 122 and 48 <= height <= 272:
            output_string.set(f'{bmi:.2f}')
            if 18.5 <= bmi <= 24.9:
                output_perfect.set("You're just perfect 🙂")
            elif bmi > 24.9:
                output_perfect.set("You are overweight, consider regular workouts!")
            else:
                output_perfect.set("You are underweight, ensure a nutritious diet.")
        else:
            messagebox.showerror('Invalid Entry', 'Age must be 1-122 years, Height must be 48-272 cm')
    except ValueError:
        messagebox.showerror('Invalid Input', 'Please enter valid numeric values for age, height, and weight')

def reset():
    age_entry.delete(0, END)
    height_entry.delete(0, END)
    weight_entry.delete(0, END)
    output_string.set("")
    output_perfect.set("")

w = Tk()
w.title('BMI Calculator App')
w.geometry('925x500+300+200')
w.configure(background='white')

try:
    icon = PhotoImage(file='bmi_icon.png')
    w.iconphoto(True, icon)
except Exception as e:
    print("Icon not found.")

try:
    photo = PhotoImage(file='BMIWavy_Lst.png').subsample(20, 20)
    photo_label = Label(w, bg='white', image=photo)
    photo_label.place(x=50, y=0)
except Exception as e:
    print("Photo not found.")

frame = Frame(w, width=500, height=400, bg='white')
frame.place(x=550, y=60)
headline = Label(w, text='BMI Calculator', bg='white', font=('Calibri', 25, 'bold'), fg='#57a1f8')
headline.place(x=600, y=80)

age_label = Label(frame, text='Age (in years)', bg='white', font=('Calibri', 10))
age_label.place(x=20, y=100)
age_entry = Entry(frame, width=11, border=0, font=('Calibri', 10))
age_entry.place(x=20, y=130)
year_label = Label(frame, text='years', bg='white')
year_label.place(x=100, y=130)
Frame(frame, width=80, height=1, bg='black').place(x=20, y=150)

height_label = Label(frame, text='Height (cm)', bg='white', font=('Calibri', 10))
height_label.place(x=20, y=200)
height_entry = Entry(frame, width=11, border=0, font=('Calibri', 10))
height_entry.place(x=20, y=220)
Frame(frame, width=80, height=1, bg='black').place(x=20, y=240)

weight_label = Label(frame, text='Weight (kg)', bg='white', font=('Calibri', 10))
weight_label.place(x=200, y=200)
weight_entry = Entry(frame, width=11, border=0, font=('Calibri', 10))
weight_entry.place(x=200, y=220)
Frame(frame, width=80, height=1, bg='black').place(x=200, y=240)

button = Button(w, text='Calculate BMI', width=30, border=0, bg='#57a1f8', command=calc, cursor='hand2')
button.place(x=600, y=350)

reset_button = Button(w, text='Reset', width=30, border=0, bg='#f85757', command=reset, cursor='hand2')
reset_button.place(x=600, y=400)

output_string = StringVar()
output = Label(w, font=('Calibri', 20), bg='white', textvariable=output_string)
output.place(x=650, y=450)

output_perfect = StringVar()
output1 = Label(w, font=('Calibri', 20), bg='white', fg='#57a1f8', textvariable=output_perfect)
output1.place(x=90, y=380)

w.mainloop()