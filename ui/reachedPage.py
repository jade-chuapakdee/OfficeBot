import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import historyFileManger

class Reached(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill="both", expand=True)
        self.configure(bg="#E5D0CC")

        style = ttk.Style()
        style.theme_use("combostyle")

        # Variables for labels
        document_form_label_text = tk.StringVar(self)
        tray_number_label_text = tk.StringVar(self)

        file_manager = historyFileManger.HistoryFileManager()
        path = master.shared_path.get()
        cost = master.shared_cost.get()

        def on_click_accept():
            print("accept button clicked")
            status = "Accepted"
            file_manager.save_history(path, cost, status)
            master.switch_frame("StartPage")

        def on_click_reject():
            result = simpledialog.askstring("Input", "Enter your reason:")
            if result:
                print("User entered:", result)
                master.shared_reason.set(result)
                status = "Rejected"
                file_manager.save_history(path, cost, status)
                self.master.switch_frame("PageReject")
            else:
                print("User canceled the input.")
            print("reject button clicked")

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

        # label2
        label2_text = "Tray Number:"
        label2 = tk.Label(self, text=label2_text, bg='#E5D0CC', fg="#444554", font=("Ubuntu", 22, "bold"))
        label2.place(x=245, y=225)
        
        labelTray_text = master.shared_tray.get()
        labelTray = tk.Label(self, text=labelTray_text, bg='#E5D0CC', fg="red", font=("Ubuntu", 22, "bold"))
        labelTray.place(x=450, y=225)
        
        # Red Rectangle
        bottom_frame = tk.Frame(bg="#f48686", width=425, height=100)
        bottom_frame.place(x=250, y=280)

        label3_text = "Please click CONFIRM after receive package"   
        label3 = tk.Label(bottom_frame, text= label3_text,fg="black", bg="#f48686" , font=("Ubuntu",14))
        label3.place(x = 15, y = 25)
        
        label4_text = "Please click REJECT if you are not the reciever"   
        label4 = tk.Label(bottom_frame, text= label4_text,fg="black", bg="#f48686" , font=("Ubuntu",14))
        label4.place(x = 15, y = 50)


        
        
        # accept button
        accept_button = tk.Button(self, text = "Confirm", command = on_click_accept, width=12, height=1,
                                 bg="#BFACB5", fg="green", font=("Ubuntu", 18, "bold"), border=2)
        accept_button.pack(pady=10)
        accept_button.place(x=250, y=395)
        
        # reject button
        reject_button = tk.Button(self, text = "Reject", command = on_click_reject, width=12, height=1,
                                 bg="#BFACB5", fg="#FF0000", font=("Ubuntu", 18, "bold"), border=2)
        reject_button.pack(pady=10)
        reject_button.place(x=483, y=395)
