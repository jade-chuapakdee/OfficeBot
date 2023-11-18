import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("First Page")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg = "#e6bb95")


def on_click_accept():
    #will define later
    print("accept button clicked")

def on_click_reject():
    #will define later
    print("reject button clicked")

label1_text = "Documents from: "
label1 = tk.Label(root, text= label1_text,bg='#e6bb95' , font=("Helvetica",16))
label1.place(x = 165, y = 50)

label2_text = "tray number: "
label2 = tk.Label(root, text= label2_text,bg='#e6bb95' , font=("Helvetica",16))
label2.place(x = 165, y = 130)

bottom_frame = tk.Frame(bg="#f48686", width=400, height=100)
bottom_frame.place(x=175, y=200)

label3_text = "Please click accept after receive package"
label3 = tk.Label(bottom_frame, text= label3_text,fg="black", bg="#f48686" , font=("Helvetica",14))
label3.place(x = 20, y = 10)

label4_text = "Please click reject if you are not the receiver"
label4 = tk.Label(bottom_frame, text= label4_text,fg="black", bg="#f48686" , font=("Helvetica",14))
label4.place(x = 10, y = 50)


accept_button = tk.Button(root, text = "Confirm", command = on_click_accept, width = 10, height = 1, bg = "#83c6d2", fg = "black", font=("Helvetica",16, "bold"), borderwidth=1)
accept_button.pack(pady=10)
accept_button.place(x=200, y=350)

reject_button = tk.Button(root, text = "Reject", command = on_click_reject, width = 10, height = 1, bg = "#83c6d2", fg = "black", font=("Helvetica",16, "bold"), borderwidth=1)
reject_button.pack(pady=10)
reject_button.place(x=400, y=350)




root.mainloop()