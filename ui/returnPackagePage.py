import tkinter as tk
from PIL import Image, ImageTk
from deliverPackagePage import DeliverPackage
import ast
import my_prolog

class ReturnPage(DeliverPackage):
    def __init__(self, master):
        super().__init__(master)

    def create_top_text_label(self):
        label_top_text = "Returning package"
        label_top = tk.Label(self.top_frame, text= label_top_text,bg='#7F7B82' , fg = "#FFFFFF", font=('Ubuntu',32, "bold"))
        label_top.place(x = 46, y = 23)
    
    def create_path_details_label(self):
        label1_text = "Destination: " + self.master.shared_from.get()
        label1 = tk.Label(self, text= label1_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label1.place(x = 755, y = 150)
        
        label2_text = "Source: " + self.master.shared_destination.get()
        label2 = tk.Label(self, text= label2_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label2.place(x = 755, y = 200)
        
        label3_text = "Tray number: " + self.master.shared_tray.get()
        label3 = tk.Label(self, text= label3_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label3.place(x = 755, y = 250)

    def start_draw_path(self):
        return_path = self.get_return_path()['Path']
        self.draw_path(return_path, self.vertexes, self.edges, 0) 
    
    def get_return_path(self):
        prolog = my_prolog.MyProlog()
        src = self.master.shared_destination.get().lower()
        des = self.master.shared_from.get().lower()
        result = prolog.getPathDetails(src, des)
        return result
    
    def change_page_to(self):
        self.after(5000, lambda: self.master.switch_frame("PageReject"))

if __name__ == "__main__":
    app = ReturnPage()
    app.mainloop()