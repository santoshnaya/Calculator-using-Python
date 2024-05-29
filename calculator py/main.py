import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

        self.number_entry = tk.Entry(master, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, borderwidth=4)
        self.number_entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, val, row, col):
        if val == '=':
            btn = tk.Button(self.master, text=val, font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, 
                            command=lambda: self.calculate()).grid(row=row, column=col)
        elif val == 'C':
            btn = tk.Button(self.master, text=val, font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, 
                            command=lambda: self.clear()).grid(row=row, column=col)
        else:
            btn = tk.Button(self.master, text=val, font=('arial', 20, 'bold'), bd=8, padx=16, pady=16, 
                            command=lambda: self.click(val)).grid(row=row, column=col)

    def click(self, val):
        self.result = False
        first_char = self.number_entry.get()
        second_char = str(val)
        
        if self.input_value:
            self.current = second_char
            self.input_value = False
        else:
            if second_char == '.' and second_char in first_char:
                return
            self.current = first_char + second_char
        self.display(self.current)

    def clear(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def display(self, value):
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, value)

    def calculate(self):
        self.result = True
        try:
            self.current = str(eval(self.current))
            self.display(self.current)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear()
            
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
