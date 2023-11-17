import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("First Page")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg = "#e6bb95")

# Create a style for the Combobox
style = ttk.Style()
style.theme_create("combostyle", parent="alt", settings={
    "TCombobox": {
        "configure": {
            "selectbackground": "#f48686",
            "fieldbackground": "#f48686",
            "bordercolor": "#f48686",
            "arrowcolor": '#090a14',
            "padding": 5,
        },
         "map": {
            "background": [("active", "#f48686")],  # Background color when the Combobox is active
            "foreground": [("!disabled", "000000")],  # Text color
        }
    }
})
style.theme_use("combostyle")




#functions
def confirm_button_click():
    #will define later
    print("confirm button clicked")





# label1
label1_text = "Destination"
label1 = tk.Label(root, text= label1_text,bg='#e6bb95' , font=("Helvetica",16))
label1.place(x = 150, y = 50)

# label2
label2_text = "Sender seat"
label2 = tk.Label(root, text= label2_text,bg='#e6bb95' , font=("Helvetica",16))
label2.place(x = 150, y = 130)

#label3
label3_text = "Tray no."
label3 = tk.Label(root, text= label3_text,bg='#e6bb95' , font=("Helvetica",16))
label3.place(x = 150, y = 200)

#list of options
destination_list = ["Please enter your destination","A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
sender_seat_list = ["Please enter your seat number","A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
tray_number_list = ["Select empty tray","1","2","3","4","5"]

#variable to store selected option
destination_option = tk.StringVar(root)
sender_option = tk.StringVar(root)
tray_option = tk.StringVar(root)

#set default option
destination_option.set(destination_list[0])
sender_option.set(sender_seat_list[0])
tray_option.set(tray_number_list[0])


destination_menu = ttk.Combobox(root, textvariable = destination_option, values = destination_list, width = 30)
destination_menu.pack(pady=10)
destination_menu.place(x = 350, y = 55)
sender_menu = ttk.Combobox(root, textvariable = sender_option, values = sender_seat_list, width = 30)
sender_menu.pack(pady=10)
sender_menu.place(x = 350, y = 135)
tray_menu = ttk.Combobox(root, textvariable = tray_option, values = tray_number_list, width = 30)
tray_menu.pack(pady=10)
tray_menu.place(x = 350, y = 205)




root.mainloop()