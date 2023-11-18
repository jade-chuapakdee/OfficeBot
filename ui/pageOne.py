import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        

if __name__ == "__main__":
    app = PageOne()
    app.mainloop()