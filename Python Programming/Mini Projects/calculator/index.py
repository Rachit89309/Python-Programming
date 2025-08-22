from tkinter import Tk, Entry, Button, StringVar, Frame, Listbox, Scrollbar, Toplevel

# Define a Calculator class that manages the calculator's UI and functionality
class Calculator:
    def __init__(self, master):
        # Set up the main window(title, size, background color, and resizing options)
        master.title("Calculator")
        master.geometry('357x470+0+0')   # width  x Height + X_offset + Y_offset
        master.config(bg='grey')    # Background color of the main window
        master.resizable(False, False)   # Disable window resizing

        self.equation = StringVar()   # To hold and update the equation or result
        self.entry_value = ''     # Stores the current value or expression
        self.history = []  # Initialize a list to store history
        
        # Frame to simulate a light blue background for the entry box
        entry_frame = Frame(master, bg='lightblue', padx=2, pady=2)
        entry_frame.place(x=0, y=0, width=357, height=60)
        
        # Entry widget where the user sees the input and result
        Entry(entry_frame, width=17, bg='lightblue', font=('Arial Bold', 28), textvariable=self.equation, borderwidth=0, highlightthickness=0).pack()

        # Create buttons for numbers, operators, and other functionalities, placing them on the window
        buttons = [
            ('(', 0, 70), (')', 90, 70), ('%', 180, 70), ('/', 270, 70),
            ('7', 0, 145), ('8', 90, 145), ('9', 180, 145), ('*', 270, 145),
            ('4', 0, 220), ('5', 90, 220), ('6', 180, 220), ('-', 270, 220),
            ('1', 0, 295), ('2', 90, 295), ('3', 180, 295), ('+', 270, 295),
            ('0', 90, 370), ('.', 180, 370), ('=', 270, 370), ('C', 0, 370),
            ('History', 0, 430)
        ]
        
        for (text, x, y) in buttons:
            Button(master, width=11, height=4, text=text, relief='flat', bg='white' if text not in ('=', 'C', 'History') else 'lightblue', 
                   command=lambda t=text: self.click(t)).place(x=x, y=y)
    
    def click(self, text):
        if text == '=':
            self.solve()
        elif text == 'C':
            self.clear()
        elif text == 'History':
            self.show_history()
        else:
            self.show(text)

    # Method to display the button values in the entry box
    def show(self, value):
        self.entry_value += str(value)  # Append the button's value to the current entry
        self.equation.set(self.entry_value)   # Update the entry display  

    # Method to clear the entry box
    def clear(self):
        self.entry_value = ''   # Clear the stored value
        self.equation.set(self.entry_value)  # Clear  the entry display

    # Method to solve the expression entered by the user
    def solve(self):
        try:
            result = eval(self.entry_value)   # Evaluate the expression
            self.equation.set(result)   # Display the result
            # Add the current expression and result to the history
            self.history.append(f"{self.entry_value} = {result}")
            self.entry_value = str(result)  # Reset entry_value to result for continued calculations
        except:
            self.equation.set("Error")   # If there's an error, show "Error" in the entry box
            self.entry_value = ""

    # Method to display the calculation history
    def show_history(self):
        # create a new window to display history
        history_window = Toplevel()
        history_window.title("History")
        history_window.geometry('300x400')

        scrollbar = Scrollbar(history_window)
        scrollbar.pack(side='right', fill='y')

        listbox = Listbox(history_window, yscrollcommand=scrollbar.set, font=('Arial', 14))
        listbox.pack(fill='both', expand=True)

        # Insert each item from history into the listbox
        for item in self.history:
            listbox.insert('end', item)

        scrollbar.config(command=listbox.yview)    

# Create the main window and run the calculator application            
root = Tk()
calculator = Calculator(root)
root.mainloop()
