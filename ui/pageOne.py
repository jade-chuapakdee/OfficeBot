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
        #will delete later
        def on_click():
            master.switch_frame("PageTwo")
            
        my_button = tk.Button(top_frame, text="Next", command=on_click)
        my_button.pack()
        my_button.place(x=800, y=50)
        
        label_top_text = "Package is on the way"
        label_top = tk.Label(top_frame, text= label_top_text,bg='#7F7B82' , fg = "#FFFFFF", font=('Ubuntu',32, "bold"))
        label_top.place(x = 46, y = 23)
        
        label1_text = "Destination: " + master.shared_destination.get()
        label1 = tk.Label(self, text= label1_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label1.place(x = 755, y = 150)
        
        label2_text = "Source: " + master.shared_from.get()
        label2 = tk.Label(self, text= label2_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label2.place(x = 755, y = 200)
        
        label3_text = "Tray number: " + master.shared_tray.get()
        label3 = tk.Label(self, text= label3_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label3.place(x = 755, y = 250)
        
        # path for circles icon
        blue_cir_path = "ui/image/blue_circle.png"
        green_cir_path = "ui/image/green_circle.png"
        red_cir_path = "ui/image/red_circle.png"
        
        blue_img = Image.open(blue_cir_path)
        blue_img = ImageTk.PhotoImage(blue_img)
        
        green_img = Image.open(green_cir_path)
        green_img = ImageTk.PhotoImage(green_img)
        
        red_img = Image.open(red_cir_path)
        red_img = ImageTk.PhotoImage(red_img)
        
        img_label_green = tk.Label(self, image=green_img,bg='#E5D0CC')
        img_label_green.image = green_img
        img_label_green.pack()
        img_label_green.place(x=755, y=330)
        

        img_label_blue = tk.Label(self, image=blue_img,bg='#E5D0CC')
        img_label_blue.image = blue_img
        img_label_blue.pack()
        img_label_blue.place(x=755, y=380)
        
        img_label_red = tk.Label(self, image=red_img,bg='#E5D0CC')
        img_label_red.image = red_img
        img_label_red.pack()
        img_label_red.place(x=755, y=430)
        
        green_label = tk.Label(self, text="= Source",bg='#E5D0CC',fg="#444554" , font=('Ubuntu',12))
        blue_label = tk.Label(self, text="= Paths",bg='#E5D0CC',fg="#444554" , font=('Ubuntu',12))
        red_label = tk.Label(self, text="= Destination",bg='#E5D0CC',fg="#444554" , font=('Ubuntu',12))
        
        green_label.place(x=795, y=335)
        blue_label.place(x=795, y=385)
        red_label.place(x=795, y=435)
        
        img = Image.open("ui/image/graph_750x421.png")
        self.background_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0,0, anchor=tk.NW, image=self.background_image)
       
        

if __name__ == "__main__":
    app = PageOne()
    app.mainloop()

