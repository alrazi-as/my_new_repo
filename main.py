import tkinter as tk
import database_handler
from registration_form import RegistrationForm
from student_listing import studentListing

class MainApplication(tk.Tk): # inharitence tk from TK class
    def __init__(self):
        super().__init__() # SUPER is an insance of perant class (tkinter)
        self.title("Students Mangement System ")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_label =tk.Label(self,text="Students Mangement System " , font=('title_font',30) ,pady= 20)
        title_label.pack(side='top' ,fill= 'x')

        self.registration_form = RegistrationForm(self, self.refresh_listing) #new instance form
        self.registration_form.pack(side = 'left' ,fill= 'y',expand= True,padx= 5 , pady= 150 )

        self.student_listing = studentListing(self)
        self.student_listing.pack(side= 'right' , fill='both',expand= True  )
 

    def refresh_listing(self):
        self.student_listing.load_students()

if __name__ == '__main__':
    app = MainApplication() # app is an instance of main application 
    app.mainloop()

