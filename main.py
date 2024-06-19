from tkinter import *

#Create our screen
screen = Tk()
screen.minsize(width=500, height=400)
screen.title("Welcome to BMI calculator")
screen.config(pady=10)

#first add a label
weight_enter = Label(text="Enter your weight(kg)")
weight_enter.config(pady=10)
weight_enter.pack()

#create an entry screen for input weight
weight = Entry()
weight = float(weight.get())
weight.pack()


#label for height
height_enter = Label(text="Enter your height(cm)")
height_enter.config(pady=10)
height_enter.pack()

#create an entry screen for input weight
height = Entry()
height.pack()

#define a function for calculate BMI
def bmi_calculator():
    bmi = weight/(height*height)

#create a button to calculate
calculate_button = Button(text="Calculate",command=bmi_calculator)
calculate_button.config(padx=10)
calculate_button.pack()







screen.mainloop()