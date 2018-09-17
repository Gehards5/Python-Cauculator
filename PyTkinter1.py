from tkinter import *
from tkinter import ttk

class Cauculator:

    calcValue = 0.0

    mathChoice = 0 

    def buttonPress(self, value):


        entryValue = self.numberEntry.get()
        entryValue += value

        self.numberEntry.delete(0, "end")
        self.numberEntry.insert(0, entryValue)


    def isDouble(self, string1): 
        try:
            float(string1)

            return True
        except ValueError:
            return False

    def mathButtonPress(self, value):

        EntryValue = str(self.numberEntry.get()) 

        if self.isDouble(EntryValue):
            self.mathChoice = 0

            self.calcValue = float(EntryValue)

            if value == "+": 
                self.mathChoice = 1
            elif value == "-": 
                self.mathChoice = 2
            elif value == "*": 
                self.mathChoice = 3
            elif value == "/": 
                self.mathChoice = 4
            
            self.numberEntry.delete(0, "end")

    def equalButtonPress(self):

        secondValue = float(self.entryValue.get())

        if self.mathChoice != 0:

            if self.mathChoice == 1:
                solution = self.calcValue + secondValue
            elif self.mathChoice == 2:
                solution = self.calcValue - secondValue
            elif self.mathChoice == 3:
                solution = self.calcValue * secondValue
            elif self.mathChoice == 4:
                solution = self.calcValue / secondValue
    
        self.numberEntry.delete(0, "end")
        self.numberEntry.insert(0, solution)

    def clearButtonPress(self):

        self.numberEntry.delete(0, "end")

    def __init__(self, root):

        self.entryValue = StringVar(root, value="")

        root.title("First Cauculator For Developer")
        root.geometry("700x300+200+200")

        root.resizable(width=False, height=False)

        stylle = ttk.Style()
        stylle.configure("TButton", font="Italic 18", padding=12)
        stylle.configure("TEntry", font="Serif 18", padding=12)

        self.numberEntry = ttk.Entry(root, textvariable=self.entryValue, width=50)
        self.numberEntry.grid(row=0, columnspan=4)

        #    1st row
        self.button7 = ttk.Button(root, text="7", command = lambda: self.buttonPress("7")).grid(row =1, column=0)
        self.button8 = ttk.Button(root, text="8", command = lambda: self.buttonPress("8")).grid(row =1, column=1)
        self.button9 = ttk.Button(root, text="9", command = lambda: self.buttonPress("9")).grid(row =1, column=2)
        self.buttonDiv = ttk.Button(root, text="/", command = lambda: self.mathButtonPress("/")).grid(row =1, column=3)

        #   2nd row
        self.button4 = ttk.Button(root, text="4", command = lambda: self.buttonPress("4")).grid(row =2, column=0)
        self.button5 = ttk.Button(root, text="5", command = lambda: self.buttonPress("5")).grid(row =2, column=1)
        self.button6 = ttk.Button(root, text="6", command = lambda: self.buttonPress("6")).grid(row =2, column=2)
        self.buttonMult = ttk.Button(root, text="*", command = lambda: self.mathButtonPress("*")).grid(row =2, column=3)

        #   3rd row
        self.button1 = ttk.Button(root, text="1", command = lambda: self.buttonPress("1")).grid(row =3, column=0)
        self.button2 = ttk.Button(root, text="2", command = lambda: self.buttonPress("2")).grid(row =3, column=1)
        self.button3 = ttk.Button(root, text="3", command = lambda: self.buttonPress("3")).grid(row =3, column=2)
        self.buttonAdd = ttk.Button(root, text="+", command = lambda: self.mathButtonPress("+")).grid(row =3, column=3)

         #   4th row
        self.buttonClear = ttk.Button(root, text="AC", command = lambda: self.clearButtonPress()).grid(row =4, column=0)
        self.button0 = ttk.Button(root, text="0", command = lambda: self.buttonPress("0")).grid(row =4, column=1)
        self.buttonEqual = ttk.Button(root, text="=", command = lambda: self.equalButtonPress()).grid(row =4, column=2)
        self.buttonSub = ttk.Button(root, text="-", command = lambda: self.mathButtonPress("-")).grid(row =4, column=3)

root = Tk()
calc = Cauculator(root)
root.mainloop()



        

 