import tkinter as tk
from database_handler import DatabaseHandler
from tkinter import ttk

class RegistrationForm(tk.Frame):
    def __init__(self,parent): # parent is instance (MainApplication)
        super().__init__(parent , padx= 10 , pady= 10)

        tk.Label(self, text =' FULL NAME ').pack(fill='x' )
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(fill='x')

        tk.Label(self,text =' Email ').pack(fill='x')
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(fill='x')


        tk.Label(self,text =' Age ').pack(fill='x')
        self.age_spinbox = ttk.Spinbox(self,from_=18, to=100)
        self.age_spinbox.pack(fill='x')


        tk.Label(self,text =' Gender ').pack(fill='x')
        self.gender_rb = tk.StringVar()
        tk.Radiobutton (self ,text="Male",variable=self.gender_rb , value= 'Male').pack(anchor='w')
        tk.Radiobutton (self ,text= "Female ",variable=self.gender_rb ,value= 'Female').pack(anchor='w')
        
        self.submit_button = tk.Button(self , text='Submit',command=self.submit_form) # submit_button as a reference just not as a function
        self.submit_button.pack(fill='x')


    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_spinbox.get()
        gender = self.gender_rb.get()

        if name and email and age and gender :
            DatabaseHandler.insert_student(name,email,age,gender)

            self.reset_form()

    def reset_form(self):
        self.name_entry.delete(0,'end')
        self.email_entry.delete(0,'end')
        self.age_spinbox.set(18)
        self.gender_rb.set(None)