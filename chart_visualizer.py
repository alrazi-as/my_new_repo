import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database_handler import DatabaseHandler

class ChartVisualizer():
    @staticmethod
    def show_gender_distribution(parent_window):
        gender_data = DatabaseHandler.get_gender_distribution()

        labels = [ row[0] for row in gender_data]
        values = [ row[1] for row in gender_data]
        

        #craete window
        chart_window = tk.Toplevel(parent_window)
        chart_window.title("Gender Distribution")
        chart_window.geometry("600x500")

        #craete matplotlab figer
        fig = Figure(figsize=(8,6),dpi=100)
        ax=fig.add_subplot(111)

        # Create pie chart
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        wedges,text,autotexts = ax.pie(values , labels = labels , autopct = '%1.1f%%',startangle=90,
                                       colors = colors[:len (labels)])
        # custimize the chart
        ax.set_title('Student Gender Distribution' , fontsize = 16 , fontweight='bold')
        

        # make percentage text more raedable
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')


        # creat canvas and add to window 
        canvas=FigureCanvasTkAgg(fig , chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)

        # Add a close button 
        close_btn = tk.Button(chart_window,text= 'Close',command= chart_window.destroy,font=('Arial',12))
        close_btn.pack(pady=10)