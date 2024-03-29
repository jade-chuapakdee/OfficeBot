import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import my_prolog

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        self.configure(bg = "#E5D0CC")
         # Check if the theme already exists
        existing_themes = ttk.Style().theme_names()
        if "combostyle" not in existing_themes:
            # If the theme doesn't exist, create it
            style = ttk.Style()
            style.theme_create("combostyle", parent="alt", settings={
                "TCombobox": {
                    "configure": {
                        "selectbackground": "#BFACB5",
                        "fieldbackground": "#BFACB5",
                        "bordercolor": "#BFACB5",
                        "arrowcolor": '#BFACB5',
                        "padding": 5,
                    },
                    "map": {
                        "background": [("active", "#BFACB5")],  # Background color when the Combobox is active
                        "foreground": [("!disabled", "#172121")],  # Text color
                    }
                }
            })
        
        style = ttk.Style()
        style.theme_use("combostyle")

        # Variables for comboboxes
        destination_option = tk.StringVar(self)
        sender_option = tk.StringVar(self)
        

        # Set default options
        destination_option.set("Please enter your destination")
        sender_option.set("Please enter your seat number")
        

    
        def confirm_button_click():

            if (
                destination_option.get() == "Please enter your destination"
                or sender_option.get() == "Please enter your seat number"
            ):
                messagebox.showwarning("Warning", "Please select all options")
            elif destination_option.get() == sender_option.get():
                messagebox.showwarning("Warning", "Destination and sender seat cannot be the same")
            else:
                master.shared_destination.set(destination_option.get())
                master.shared_from.set(sender_option.get())
                src = master.shared_from.get().lower()
                des = master.shared_destination.get().lower()
                
                room_dict = {
                    "a": "(0,0)",
                    "b": "(0,2)",
                    "c": "(4,2)",
                    "d": "(0,4)",
                    "e": "(4,5)",
                    "f": "(9,1)",
                    "g": "(9,3)",
                }

                print("Source:", room_dict[src], "Destination:", room_dict[des])
                prolog = my_prolog.MyProlog()
                path = prolog.getPathDetails(room_dict[src], room_dict[des])
                master.shared_path.set(path)
                master.switch_frame("DeliverPage")

            
            

        def clear_button_click():
            # Reset combobox options
            destination_option.set(destination_list[0])
            sender_option.set(sender_seat_list[0])
            
        def history_button_click():
            master.switch_frame("HistoryPage")
        
        top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)   
        top_frame.place(x=0, y=0) 
        

        label_top_text = "OfficeBot"
        label_top = tk.Label(top_frame, text= label_top_text,bg='#7F7B82' ,fg="#FFFFFF" , font=('Ubuntu',32, "bold"))
        label_top.place(x = 369, y = 22)
        
        label1_text = "Destination"
        label1 = tk.Label(self, text= label1_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',22, "bold"))
        label1.place(x = 177, y = 174)

        # label2
        label2_text = "Sender seat"

        label2 = tk.Label(self, text= label2_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',22, "bold"))

        label2.place(x = 177, y = 235)

            
        #list of options
        destination_list = ["Please enter your destination","A","B","C","D","E","F","G"]
        sender_seat_list = ["Please enter your seat number","A","B","C","D","E","F","G"]
        
        #variable to store selected option
        destination_option = tk.StringVar(self)
        sender_option = tk.StringVar(self)    
            
            
        #set default option
        destination_option.set(destination_list[0])
        sender_option.set(sender_seat_list[0])    
            
        #combobox
        destination_menu = ttk.Combobox(self, textvariable = destination_option, values = destination_list, width = 30)
        destination_menu.pack(pady=10)
        destination_menu.place(x = 420, y = 176)

        destination_menu.config(font=('Ubuntu', 12),foreground="#444554")

        
        sender_menu = ttk.Combobox(self, textvariable = sender_option, values = sender_seat_list, width = 30)
        sender_menu.pack(pady=10)
        sender_menu.place(x = 420, y = 237)
        sender_menu.config(font=('Ubuntu', 12),foreground="#444554")
        
        self.history_icon_path = "ui/image/history_icon.png"
        self.history_icon = Image.open(self.history_icon_path)
        self.history_icon = ImageTk.PhotoImage(self.history_icon)

        # Create the button using the image
        history_button = tk.Button(self, image=self.history_icon, command=history_button_click, bg="#E5D0CC",bd=0,highlightthickness=0)
        history_button.pack()
        history_button.place(x=680, y=345)  
            
        #confirm button
        confirm_button = tk.Button(self, text = "Confirm", command = confirm_button_click, width = 12, height = 1, bg = "#BFACB5", fg = "#02FF3A", font=('Ubuntu',18, "bold"), border=2)

        confirm_button.pack(pady=10)
        confirm_button.place(x = 250, y = 395)
        
        #clear button 

        clear_button = tk.Button(self, text = "Clear", command = clear_button_click, width = 12, height = 1, bg = "#BFACB5", fg = "#FF0000", font=('Ubuntu',18,"bold"), border=2)
        clear_button.pack(pady=10)
        clear_button.place(x = 483, y = 395)   