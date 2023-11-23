import tkinter as tk
import historyFileManger

class HistoryPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#E5D0CC")
        self.pack(fill="both", expand=True)
        
        def on_click_back():
            master.switch_frame("StartPage")
        
        top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)
        top_frame.place(x=0, y=0)
        
        frame_label = tk.Label(top_frame, text="Delivery History", bg='#7F7B82', fg="#FFFFFF", font=("Ubuntu", 32, "bold"))
        frame_label.place(x=46, y=24)
        
        #first row
        source_label = tk.Label(self, text="Source", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        source_label.place(x=20, y=120)
        
        destination_label = tk.Label(self, text="Destination", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        destination_label.place(x=100, y=120)
        
        cost_label = tk.Label(self, text="Cost", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        cost_label.place(x=230, y=120)
        
        path_label = tk.Label(self, text="Path", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        path_label.place(x=325, y=120)
        
        time_label = tk.Label(self, text="Time", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        time_label.place(x=635, y=120)
        
        status_label = tk.Label(self, text="Status", bg='#E5D0CC', fg="#444554", font=("Ubuntu", 12, "bold"))
        status_label.place(x=800, y=120)
        ###
        
        file_manager = historyFileManger.HistoryFileManager()
        history = file_manager.read_history()
        
        for i in range(len(history)):
            data = history[i]
            y_offset = 30 * i

            src = tk.Label(self, text=data[0].upper(), bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            src.place(x=40, y=150 + y_offset)

            des = tk.Label(self, text=data[1].upper(), bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            des.place(x=135, y=150 + y_offset)

            cost = tk.Label(self, text=data[2], bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            if int(data[2]) < 0:
                cost.place(x=243, y=150 + y_offset)
            else:
                cost.place(x=247, y=150 + y_offset)


            path = tk.Label(self, text=data[3], bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            path.place(x=325, y=150 + y_offset)

            time = tk.Label(self, text=data[4], bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            time.place(x=635, y=150 + y_offset)

            status = tk.Label(self, text=data[5], bg='#E5D0CC', fg="#444554", font=("Ubuntu", 10))
            status.place(x=800, y=150 + y_offset)

        back_button = tk.Button(self, text="Back", command=on_click_back, width=10, height=1,bg="#BFACB5", fg="#444554", font=("Ubuntu", 18, "bold"), border=2)
        
        back_button.place(x=385, y=441)
        
        
        
      
