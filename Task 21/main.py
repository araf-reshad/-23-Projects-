from tkinter import *
import random

window = Tk()
window.title("Dice Roller")

# Initialize variables for number of sides on the dice, number of dice, and whether or not to show the sum of dice
radio_button_status = IntVar(value=6)
num_dice = IntVar(value=2)
show_sum = BooleanVar(value=False)

def roll_dice():
    """Simulate a dice roll and display the results"""
    
    # Assign the selected number of sides
    num_sides = radio_button_status.get()

    # Create a list of random numbers each representing a dice roll
    results = [random.randint(1, num_sides) for _ in range(num_dice.get())]

    # If show_sum is true, display the sum of the dice rolls along with the dice rolls
    if show_sum.get():
        result_string = " + ".join(map(str, results)) + " = " + str(sum(results))
    else:
        result_string = ", ".join(map(str, results))

    # Update the result label to show dice rolls (and sum, if chosen)
    result_label.config(text="You rolled " + result_string)
  

# Create radio buttons for selecting the number of sides on the dice
Radiobutton(window, text="4", variable=radio_button_status, value=4).grid(row=0, column=1)

Radiobutton(window, text="6", variable=radio_button_status, value=6).grid(row=0, column=2)

Radiobutton(window, text="8", variable=radio_button_status, value=8).grid(row=0, column=3)

Radiobutton(window, text="12", variable=radio_button_status, value=12).grid(row=0, column=4)

Radiobutton(window, text="20", variable=radio_button_status, value=20).grid(row=0, column=5)


# Add labels to the window.
Label(window, text="Number of sides:").grid(row=0, column=0)

# Frame to hold the radio buttons for number of sides
radio_frame = Frame(window)
radio_frame.grid(row=0, column=1)

# Add label and input field for number of dice
Label(window, text="Number of dice:").grid(row=1, column=0)
Entry(window, width=6, textvariable=num_dice).grid(row=1, column=1)

# Add button to roll the dice
Button(window, text="Roll dice", command=roll_dice).grid(row=2, column=0)

# Add checkbutton whether to show the sum of dice or not
label_show_sum = Label(window, text="Show sum")
label_show_sum.grid(row=1, column=3)
checkbox = Checkbutton(window, variable=show_sum)
checkbox.grid(row=1, column=4)

# Label to show the result of dice rolls
result_label = Label(window, text="")
result_label.grid(row=2, column=3, columnspan = 2)

mainloop()
