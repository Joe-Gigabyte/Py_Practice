from tkinter import *

root = Tk()
root.title("Insulin Calculator")
root.geometry("400x200")



def calc_function():
    show_answer = Label(calc_textbox.get())
    show_answer.grid(row=3, column=2)

   



calc_label = Label(root, text= "Enter Carb Grams - ")
calc_label.grid(row=2, column=0)

calc_textbox = Entry(root, width=3, border=5)
calc_textbox.grid(row=2, column=2)

space = Label(root, text=" ")
space.grid(row=2, column=3)

calc_button = Button(root, text="Submit", border=5, command=calc_function)
calc_button.grid(row=2, column=4)

   
  
   







root.mainloop()