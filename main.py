"""""
Joke Prompt Generator
==========================
This function helps prompt comedians with writers block by choosing a prompt at random ffrom a list of prompts. 
The function can be used with a GUI implemented with Tkinter.
"""""

# Import dependencies 
from tkinter import *
import random

def prompt_generator():
    #Read prompt file
    prompt_file = open('prompts.txt', 'r')
    prompts = prompt_file.readlines()

    #Create window
    window = Tk()

    #Center window on screen
    window.eval('tk::PlaceWindow . center')

    # Set window title
    window.title('Random Joke Prompt')

    # Set winow background color
    window.configure(bg='Pink')

    # Create labels
    label_one = Label(text='Write a joke about...', bg='Pink')
    label_one.pack()

    label_two = Label(text='', font=('Calibri', 25, 'bold'), bg='Pink')
    label_two.pack()

    # Create button function
    def generate_prompt():
        prompt = random.choice(prompts) 
        label_two.configure(text=prompt)

    #Create button
    button = Button(text='Prompt Me!', command=generate_prompt)
    button.pack()
        

    #Keeps window open
    window.mainloop()

#If this is hte main script, run the function. If not, it won't run, and can be included in another script without opening the window automatically. 
if __name__ == '__main__':
     prompt_generator()