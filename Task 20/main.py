from tkinter import *

#Size of the window 
WIDTH = 250
HEIGHT = 90

#Create window
window = Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title ("Button Counter")

#Create Click counter
click_count = 0

#Create a label to display the number of clicks 
click_label = Label(window, text=f"You've clicked the button {click_count} times")
click_label.pack()
click_label.place (x=WIDTH/2, y=HEIGHT/9+50, anchor="center" )

def increase_click():
    """
    Increments the click count by 1, updates the click_label, and disables the click_button 
    if the count reaches 9.
    """
    global click_count
    click_count += 1
    click_label["text"] = f"You've clicked the button {click_count} times"

  # Check if click_count has reached 9 and if so, disable click_button
    if click_count == 9:
      click_button["state"] = "disabled"

def reset_count():
  """
  Resets the click count to 0, updates the click_label, and re-enables the click_button.
  """
  global click_count
  click_count = 0
  click_label ["text"] = f"You've clicked the button {click_count} times"
  click_button["state"] = "normal"

#Create a button to increment the click count
click_button = Button (window, text="Click Me", command=increase_click)
click_button.pack()
click_button.place(x=WIDTH/2-50, y=HEIGHT/3, anchor= "center")

#Create a button to reset the click count
reset_button = Button(window, text="Reset", command=reset_count)
reset_button.pack()
reset_button.place(x=WIDTH/2+50, y=HEIGHT/3, anchor= "center") 
mainloop()