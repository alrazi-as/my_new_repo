import tkinter as tk
from database_handler import DatabaseHandler
from tkinter import ttk
from chart_visualizer import ChartVisualizer

from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RegistrationForm(tk.Frame):
    def __init__(self,parent , refresh_callback): # parent is instance (MainApplication)
        super().__init__(parent , padx= 10 , pady= 10)
        self.refresh_callback= refresh_callback

        tk.Label(self, text =' FULL NAME ').pack(fill='x' )
        self.name_entry = tk.Entry(self,width=30 ,font= 20 )
        self.name_entry.pack(fill='x')

        tk.Label(self,text =' Email ').pack(fill='x')
        self.email_entry = tk.Entry(self,width=30 ,font= 20 )
        self.email_entry.pack(fill='x')


        tk.Label(self,text =' Age ').pack(fill='x')
        self.age_spinbox = ttk.Spinbox(self,from_=18, to=100 ,width= 30,font=20)
        self.age_spinbox.pack(fill='x')

 
        tk.Label(self,text =' Gender ').pack(fill='x')
        self.gender_rb = tk.StringVar()
        tk.Radiobutton (self ,text="Male",variable=self.gender_rb , value= 'Male',font=20).pack(anchor='w')
        tk.Radiobutton (self ,text= "Female ",variable=self.gender_rb ,value= 'Female',font= 20 ).pack(anchor='w')
        
        self.submit_button = tk.Button(self , text='Submit',command=self.submit_form , font= 30) # submit_butt on as a reference just not as a function
        self.submit_button.pack(fill='x')

        # Add button to show gender distribution chart 
        self.chart_button = tk.Button(
            self,text= 'Show Gender Distributon',
            command=self.show_gender_chart,
            font=20,bg='lightblue')
        self.chart_button.pack(fill='x' ,pady=(10,0))
                               


    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_spinbox.get()
        gender = self.gender_rb.get()

        if not name and not email and not age and not gender:
            DatabaseHandler.delete_all_students()
            self.refresh_callback()  
            self.reset_form()

        if name and email and age and gender :
            DatabaseHandler.insert_student(name,email,age,gender)
            self.refresh_callback()

            # Reset Form
            self.reset_form()
      

    def reset_form(self):
        self.name_entry.delete(0,tk.END)
        self.email_entry.delete(0,tk.END)
        self.age_spinbox.set(18)
        self.gender_rb.set(None)

    def fetch_gender(self):
        DatabaseHandler.get_all_students()

    def show_gender_chart(self):
        ChartVisualizer.show_gender_distribution(self)