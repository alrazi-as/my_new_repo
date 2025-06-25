
import tkinter as tk
from tkinter import ttk
from database_handler import DatabaseHandler

class studentListing(tk.Frame):
    def __init__(self,parent): # parent is instance (MainApplication)
        super().__init__(parent)
        
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self,columns=('ID' , 'Name','Email','Age','Gender'),show='headings')
        self.tree.heading('ID', text= 'ID' )
        self.tree.heading('Name', text= 'Name')
        self.tree.heading('Email', text= 'Email')
        self.tree.heading('Age', text= 'Age')
        self.tree.heading('Gender', text= 'Gender')
        self.tree.pack(fill=tk.BOTH , expand= 800)
        self.load_students()


    def load_students(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for students in DatabaseHandler.get_all_students():
            self.tree.insert('', tk.END ,values= students)