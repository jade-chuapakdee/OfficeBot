import tkinter as tk

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        self.configure(bg = "#e6bb95")
        
        def on_click_return():
            #will define later
            print("return button clicked")
            master.switch_frame("StartPage")
        
        
        label1_text = "Package rejected"
        label1 = tk.Label(self, text= label1_text,bg='#e6bb95' , font=("Helvetica",16))
        label1.place(x = 300, y = 150)
        label2_text = "Reason: " + master.shared_reason.get()
        label2 = tk.Label(self, text= label2_text,bg='#e6bb95' , font=("Helvetica",16))
        label2.place(x = 300, y = 200)
        
        return_button = tk.Button(self, text = "OK", command = on_click_return, width = 10, height = 1, bg = "#83c6d2", fg = "black", font=("Helvetica",16, "bold"), borderwidth=1)
        return_button.pack(pady=10)
        return_button.place(x=310, y=250)

if __name__ == "__main__":
    app = PageThree()
    app.mainloop()