import tkinter as tk
import database_handler~

class MainApplication(tk.Tk): # inharitence tk from TK class
    def __init__(self):
        super().__init__() # SUPER is an insance of perant class (tkinter)
        self.title("Students Mangement System ")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_label =tk.Label(self,text="Students Mangement System " , font=('fancy text',60))
        title_label.pack(side='top' ,fill= 'x')

if __name__ == '__main__':
    app = MainApplication() # app is an instance of main application 
    app.mainloop()