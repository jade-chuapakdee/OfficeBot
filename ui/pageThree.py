import tkinter as tk

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#E5D0CC")
        self.pack(fill="both", expand=True)

        def on_click_return():
            print("return button clicked")
            master.switch_frame("StartPage")

        label1_text = "Package rejected"
        label1 = tk.Label(self, text=label1_text, bg='#e6bb95', font=("Helvetica", 16))
        label1.place(x=300, y=150)

        # Use master.shared_reason.get() to get the reason
        label2_text = "Reason: " + master.shared_reason.get()
        label2 = tk.Label(self, text=label2_text, bg='#e6bb95', font=("Helvetica", 16))
        label2.place(x=300, y=200)

        return_button = tk.Button(self, text="OK", command=on_click_return, width=10, height=1,
                                  bg="#83c6d2", fg="black", font=("Helvetica", 16, "bold"), borderwidth=1)
        return_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    app = PageThree(root)
    app.mainloop()
