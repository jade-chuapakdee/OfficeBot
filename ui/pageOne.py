import tkinter as tk
from PIL import Image, ImageTk
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        self.configure(bg = "#E5D0CC")
        
        self.canvas = tk.Canvas(self, width=740, height=421)
        self.canvas.pack()
        self.canvas.place(x=0, y=80)
        
        top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)   
        top_frame.place(x=0, y=0) 
        
        label_top_text = "Package is on the way"
        label_top = tk.Label(top_frame, text= label_top_text,bg='#7F7B82' , fg = "#FFFFFF", font=("Helvetica",32, "bold"))
        label_top.place(x = 46, y = 23)
        
        

        img = Image.open("ui/image/graph_750x421.png")
        self.background_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0,0, anchor=tk.NW, image=self.background_image)
       
        

if __name__ == "__main__":
    app = PageOne()
    app.mainloop()

