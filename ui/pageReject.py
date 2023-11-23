import tkinter as tk
from tkinter import ttk


class PageReject(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill="both", expand=True)
        self.configure(bg="#E5D0CC")

        top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)
        top_frame.place(x=0, y=0)

        label_top = "Package Rejected"
        label_top = tk.Label(top_frame, text=label_top, bg='#7F7B82', fg="#FFFFFF", font=("Ubuntu", 32, "bold"))
        label_top.place(x=40, y=22)

        label1_text = "Your Package is"
        label1 = tk.Label(self, text=label1_text, bg='#E5D0CC', fg="#444554", font=("Ubuntu", 26))
        label1.place(x=240, y=200)
        
        label2_text = "REJECTED"
        label2 = tk.Label(self, text=label2_text, bg='#E5D0CC', fg="red", font=("Ubuntu", 26))
        label2.place(x=500, y=200)

        # label2
        label3_text = "Reason:  "
        label3 = tk.Label(self, text=label3_text, bg='#E5D0CC', fg="#444554", font=("Ubuntu", 26))
        label3.place(x=310, y=260)
        
        labelReason_text = master.shared_reason.get()
        labelReason = tk.Label(self, text=labelReason_text, bg='#E5D0CC', fg="red", font=("Ubuntu", 26))
        labelReason.place(x=450, y=260)

        def go_back():
            master.switch_frame("StartPage")

        # Back button
        back_button = tk.Button(self, text="OK", command=go_back, width=12, height=1,
                                bg="#BFACB5", fg="green", font=("Ubuntu", 18, "bold"), border=2)
        back_button.pack(pady=10)
        back_button.place(x=370, y=395)


