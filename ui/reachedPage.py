import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import historyFileManger

class Reached(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill="both", expand=True)
        self.configure(bg="#E5D0CC")

        

        

        file_manager = historyFileManger.HistoryFileManager()
        path = master.shared_path.get()
        cost = master.shared_cost.get()

        def on_click_accept():
            status = "Accepted"
            master.switch_frame("StartPage")

        
            

        top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)
        top_frame.place(x=0, y=0)

        label_top = "Your Document is Here!"
        label_top = tk.Label(top_frame, text=label_top, bg='#7F7B82', fg="#FFFFFF", font=("Ubuntu", 32, "bold"))
        label_top.place(x=30, y=20)

        label1_text = "Document From:"
        label1 = tk.Label(self, text=label1_text, bg='#E5D0CC', fg="#444554", font=("Ubuntu", 22, "bold"))
        label1.place(x=245, y=174)
        
        labelDoc_text = master.shared_from.get()
        labelDoc = tk.Label(self, text=labelDoc_text, bg='#E5D0CC', fg="red", font=("Ubuntu", 22, "bold"))
        labelDoc.place(x=500, y=174)

        
        # Red Rectangle
        bottom_frame = tk.Frame(bg="#f48686", width=425, height=100)
        bottom_frame.place(x=250, y=280)

        label3_text = "Please click CONFIRM after receive package"   
        label3 = tk.Label(bottom_frame, text= label3_text,fg="black", bg="#f48686" , font=("Ubuntu",14))
        label3.place(x = 15, y = 40)
        
        
        
        # accept button
        accept_button = tk.Button(self, text = "Confirm", command = on_click_accept, width=12, height=1,
                                 bg="#BFACB5", fg="green", font=("Ubuntu", 18, "bold"), border=2)
        accept_button.pack(pady=10)
        accept_button.place(x=370, y=395)
        
        
