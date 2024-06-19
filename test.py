from logging import root
from os import path
from tkinter import *
from tkinter import messagebox

#create the screen
screen = Tk()
screen.config(bg="light blue")
screen.minsize(width=500, height=400)
screen.title("Welcome to BMI calculator")
screen.config(pady=10)

#first add a label
weight_enter = Label(text="Enter your weight(kg)", font= "20" "Arial", bg="light blue", pady=10)
weight_enter.pack()

#create an entry screen for input weight
weight = Entry(width=30)
weight.pack()

#label for height
height_enter = Label(text="Enter your height(cm)", font= "20" "Arial", bg="light blue",pady=10)
height_enter.pack()

#create an entry screen for input weight
height = Entry(width=30)
height.pack()

def convert_to_float(entry):
    try:
        # Get the input from the Entry widget
        input_value = float(entry.get())
        return input_value
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

#create a label to show the output
situation = Label(pady=15, bg="light blue", font= "20" "Arial")

#define a function for calculate BMI
def bmi_calculator():
    x = convert_to_float(weight)
    y = convert_to_float(height)

    y = y / 100  #turn cm to m
    bmi = x / (y * y)
    bmi = round(bmi, ndigits=2)  # round it for better visualization

    situation.config(text="")  # set the current to an empty string for new entries
    #define the situations
    if bmi < 18:
        situation.config(text=f"your BMI is {bmi} you are underweight")
    elif 18 <= bmi < 25:
        situation.config(text=f"your BMI is {bmi} you are normal")
    elif 25 <= bmi < 30:
        situation.config(text=f"your BMI is {bmi} you are overweight")
    elif 30 <= bmi < 35:
        situation.config(text=f"your BMI is {bmi} you are obese")
    else:
        situation.config(text=f"your BMI is {bmi} you are clinically obese")
    situation.pack()  #pack the result to the screen

#create a button to calculate and command it with my bmi_calculator
calculate_button = Button(text="Calculate", command=bmi_calculator, bg="yellow", font="green")
calculate_button.pack()

#add "" label for some area
space = Label(text="", width=100, bg="light blue", height=2)
space.pack()

#add image for fun
import tkinter as tk # add this necessary libraries to add photo
from PIL import Image, ImageTk

# Load the image
image_path = "bear.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image
panel = tk.Label(screen, image=photo)
panel.pack(side="bottom", fill="both")


screen.mainloop()
