import tkinter as tk
from tkinter import messagebox

# ------- Procedural Approach -------

# Create the main Tkinter window
#root = tk.Tk()

# Set the initial size and title of the window
#root.geometry("500x500")
#root.title("langTranslator")

# Create a label widget for user instructions
#label = tk.Label(root, 
#                 text="What would you like to Translate?", 
#                 font=('Arial', 18)
#                 )
#label.pack(padx=20, pady=20)

# Create a text box for user input
#textbox1 = tk.Text(root, height=10, font=('Arial', 10))
#textbox1.pack(padx=10, pady=10)

# Create a button for triggering translation
#button = tk.Button(root, text="Translate", font=('Arial', 14))
#button.pack()

# Create a text box for displaying translated output
#textbox2 = tk.Text(root, height=10, font=('Arial', 10))
#textbox2.pack(padx=10, pady=10)

# Alternatively, create a single-line entry widget
#myEntry = tk.Entry(root)
#myEntry.pack()

# Start the Tkinter event loop
#root.mainloop()


# ------- Object-Oriented Approach -------

class LTGUI:

    def __init__(self):
        # Initialize the main Tkinter window
        self.root = tk.Tk()

        # Create and pack a label widget for user instructions
        self.label = tk.Label(self.root, text="What would you like to Translate", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        # Create and pack a textbox for user input
        self.textbox = tk.Text(self.root, font=('Arial', 18), height=20)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        # Initialize a variable to hold the state of a check button
        self.check_state = tk.IntVar()

        # Create and pack a checkbox widget
        self.check = tk.Checkbutton(self.root, text="Show Message", font=('Arial',18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        # Create and pack a button widget with a callback function
        self.button = tk.Button(self.root, text="Translate", font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        #Create a text box for displaying translated output
        self.textbox2 = tk.Text(self.root, height=10, font=('Arial', 10))
        self.textbox2.pack(padx=10, pady=10)

        # Start the Tkinter event loop
        self.root.mainloop()

    def show_message(self):
        # Print message shown in textbox
        inputMessage = self.textbox.get('1.0',tk.END)
        self.textbox.delete('1.0',tk.END)
        self.textbox2.delete('1.0',tk.END)

        if self.check_state.get() == 0:
            print(inputMessage)
        else:
            messagebox.showinfo(title="message", message=inputMessage)
            
        self.textbox2.insert(tk.END, inputMessage)

    def shortcut(self, event):
        #print(event.keysym)
        #print(event.state)
        if event.state == 4 and event.keysym == "Return":
            self.show_message()

# Instantiate the LTGUI class to start the GUI
LTGUI()
