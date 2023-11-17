import tkinter as tk
root = tk.Tk()
root.title("First Page")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg = "#e6bb95")

label1_text = "Destination"
label1 = tk.Label(root, text= label1_text,bg='#e6bb95' , font=("Helvetica",16))
label1.place(x = 150, y = 50)


root.mainloop()