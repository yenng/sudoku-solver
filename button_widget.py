from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.count = 0    
        
    def create_widgets(self):
        # Creating a button widget
        myButton = Button(root, text="Click Me!", command=self.clicked)
        myExit = Button(root, text="Exit", command=root.destroy)
        
        # Shoving it onto the screen
        myButton.pack(side='top',fill=X)
        myExit.pack(side='bottom',fill=X)
        
    def clicked(self):
        # Creating function when "Click Me!" button was clicked.
        self.count += 1
        myLabel = Label(text="Clicked " + str(self.count))
        myLabel.pack()
    

root = Tk()
app = App(master=root)
app.mainloop()
