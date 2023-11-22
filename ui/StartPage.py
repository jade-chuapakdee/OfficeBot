import tkinter as tk
from tkinter import ttk
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        self.configure(bg = "#e6bb95")
         # Check if the theme already exists
        existing_themes = ttk.Style().theme_names()
        if "combostyle" not in existing_themes:
            # If the theme doesn't exist, create it
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
        
        style = ttk.Style()
        style.theme_use("combostyle")

        # Variables for comboboxes
        destination_option = tk.StringVar(self)
        sender_option = tk.StringVar(self)
        tray_option = tk.StringVar(self)

        # Set default options
        destination_option.set("Please enter your destination")
        sender_option.set("Please enter your seat number")
        tray_option.set("Select empty tray")

        # Rest of your code for labels, comboboxes, and buttons

        def confirm_button_click():
            # Your implementation here
            print("confirm button clicked")
            master.shared_from.set(sender_option.get())
            master.shared_tray.set(tray_option.get())
            master.switch_frame("PageOne")

        def clear_button_click():
            # Reset combobox options
            destination_option.set(destination_list[0])
            sender_option.set(sender_seat_list[0])
            tray_option.set(tray_number_list[0])
        
        label1_text = "Destination"
        label1 = tk.Label(self, text= label1_text,bg='#e6bb95' , font=("Helvetica",16))
        label1.place(x = 165, y = 50)

        # label2
        label2_text = "Sender seat"
        label2 = tk.Label(self, text= label2_text,bg='#e6bb95' , font=("Helvetica",16))
        label2.place(x = 165, y = 130)

        #label3
        label3_text = "Tray no."
        label3 = tk.Label(self, text= label3_text,bg='#e6bb95' , font=("Helvetica",16))
        label3.place(x = 165, y = 210)    
        
            
        #list of options
        destination_list = ["Please enter your destination","A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
        sender_seat_list = ["Please enter your seat number","A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5"]
        tray_number_list = ["Select empty tray","1","2","3","4","5"]
        
        #variable to store selected option
        destination_option = tk.StringVar(self)
        sender_option = tk.StringVar(self)
        tray_option = tk.StringVar(self)    
            
            
        #set default option
        destination_option.set(destination_list[0])
        sender_option.set(sender_seat_list[0])
        tray_option.set(tray_number_list[0])    
            
        #combobox
        destination_menu = ttk.Combobox(self, textvariable = destination_option, values = destination_list, width = 30)
        destination_menu.pack(pady=10)
        destination_menu.place(x = 365, y = 55)
        sender_menu = ttk.Combobox(self, textvariable = sender_option, values = sender_seat_list, width = 30)
        sender_menu.pack(pady=10)
        sender_menu.place(x = 365, y = 135)
        tray_menu = ttk.Combobox(self, textvariable = tray_option, values = tray_number_list, width = 30)
        tray_menu.pack(pady=10)
        tray_menu.place(x = 365, y = 215)    
            
        #confirm button
        confirm_button = tk.Button(self, text = "Confirm", command = confirm_button_click, width = 10, height = 1, bg = "#83c6d2", fg = "black", font=("Helvetica",16, "bold"), borderwidth=1)
        confirm_button.pack(pady=10)
        confirm_button.place(x = 215, y = 350)
        
        #clear button 
        clear_button = tk.Button(self, text = "Clear", command = clear_button_click, width = 10, height = 1, bg = "#83c6d2", fg = "black", font=("Helvetica",16,"bold"), borderwidth=1)
        clear_button.pack(pady=10)
        clear_button.place(x = 415, y = 350)   
            
       