from tkinter import *

window = Tk()

# Set the dimensions of the window
WIDTH = 430
HEIGHT = 470
window.geometry(f"{WIDTH}x{HEIGHT}")

# Set the title of the window
window.title("Calculator")

# Add the buttons and numbers to the window
answer_num = Label(window, text = "0", anchor = "e", width = 9, font = ("FreeMono", 35), pady = 15, borderwidth = 0, padx = 10)

answer_num.grid(row = 0, column = 0, columnspan = 4, rowspan = 2)

AC_button = Label(window, text = "AC", font = ("FreeSans", 20), pady = 20)

AC_button.grid(row = 2, column = 0)

plus_minus_button = Label(window, text = "+/-",  font = ("FreeSans", 20), padx = 15) 

plus_minus_button.grid(row=2, column = 1)

percent_button = Label(window, text = "%",  font = ("FreeSans", 20), padx = 15)

percent_button.grid(row = 2, column = 2)

division_button = Label(window, text = "÷",  font = ("FreeSans", 20))

division_button.grid(row = 2, column = 3)

seven_button = Label(window, text = "7",  font = ("FreeSans", 20))

seven_button.grid(row = 3, column = 0)

eight_button = Label(window, text = "8",  font = ("FreeSans", 20), padx = 15) 

eight_button.grid(row=3, column = 1)

nine_button = Label(window, text = "9",  font = ("FreeSans", 20), padx = 15)

nine_button.grid(row = 3, column = 2)

x_button = Label(window, text = "x",  font = ("FreeSans", 20))

x_button.grid(row = 3, column = 3)

four_button = Label(window, text = "4",  font = ("FreeSans", 20),  pady = 20)

four_button.grid(row = 4, column = 0)

five_button = Label(window, text = "5",  font = ("FreeSans", 20), padx = 15) 

five_button.grid(row=4, column = 1)

six_button = Label(window, text = "6",  font = ("FreeSans", 20), padx = 15)

six_button.grid(row = 4, column = 2)

plus_button = Label(window, text = "+",  font = ("FreeSans", 20))

plus_button.grid(row = 4, column = 3)

one_button = Label(window, text = "1",  font = ("FreeSans", 20))

one_button.grid(row = 5, column = 0)

two_button = Label(window, text = "2",  font = ("FreeSans", 20), padx = 15) 

two_button.grid(row=5, column = 1)

three_button = Label(window, text = "3",  font = ("FreeSans", 20), padx = 15)

three_button.grid(row = 5, column = 2)

minus_button = Label(window, text = "-",  font = ("FreeSans", 20))

minus_button.grid(row = 5, column = 3)

zero_button = Label(window, text = "0",  font = ("FreeSans", 20), pady = 20)

zero_button.grid(row = 6, column = 0, columnspan = 2)

decimal_button = Label(window, text = ".",  font = ("FreeSans", 20), padx = 15)

decimal_button.grid(row = 6, column = 2)

equals_button = Label(window, text = "=",  font = ("FreeSans", 20))

equals_button.grid(row = 6, column = 3)

# Keeps the window running
mainloop()
