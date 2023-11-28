import tkinter as tk
from PIL import Image, ImageTk

class DeliverPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill="both", expand=True)
        self.configure(bg="#E5D0CC")
        self.master = master

        self.canvas = tk.Canvas(self, width=800, height=320)
        self.canvas.pack()
        self.canvas.place(x=50, y=120)

        def on_click_next():
            master.switch_frame("ReachedPage")
            
        def draw_wall(x1,y1,x2,y2):
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
        
        def draw_obsatcle(x1,y1,x2,y2):
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
            
            
            

        self.top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)
        self.top_frame.place(x=0, y=0)

        self.create_top_text_label()

        self.next_icon_path = "ui/image/next_icon.png"
        self.next_icon = Image.open(self.next_icon_path)
        self.next_icon = ImageTk.PhotoImage(self.next_icon)

        next_button = tk.Button(self.top_frame, image=self.next_icon, bg='#7F7B82', bd=0, command=on_click_next,
                                highlightthickness=0)
        next_button.pack()
        next_button.place(x=830, y=35)

        # Define the number of rows and columns
        rows = 7
        columns = 9

        # Calculate the row and column heights and widths
        row_height = self.canvas.winfo_reqheight() / rows
        column_width = self.canvas.winfo_reqwidth() / columns

        # Draw horizontal grid lines
        for i in range(1, rows):
            y = i * row_height
            self.canvas.create_line(0, y, self.canvas.winfo_reqwidth(), y, fill="#7F7B82")

        # Draw vertical grid lines
        for i in range(1, columns):
            x = i * column_width
            self.canvas.create_line(x, 0, x, self.canvas.winfo_reqheight(), fill="#7F7B82")

        # Draw outline lines
        self.canvas.create_line(2, 2, 800, 2, fill="#7F7B82", width=2)  # top
        self.canvas.create_line(2, 2, 2, 320, fill="#7F7B82", width=2)  # left
        self.canvas.create_line(800, 2, 800, 320, fill="#7F7B82", width=2)  # right
        self.canvas.create_line(2, 320, 800, 320, fill="#7F7B82", width=2)  # bottom
        
        #text in cells
        self.canvas.create_text(400, 160, text="C", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 160, text="B", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 70, text="A", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 250, text="D", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(400, 300, text="E", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(750, 125, text="F", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(750, 215, text="G", font=("Helvetica", 16), fill="blue")
        
        #A
        draw_wall(2, 45, 90 , 45)
        draw_wall(2, 45, 2 , 95)
        draw_wall(2, 95, 90 , 95)
        
        #B
        draw_wall(2,140,90,140)
        draw_wall(2,140,2,185)
        draw_wall(2,185,90,185)
        
        #C
        draw_wall(358,140,358,185)
        draw_wall(358,185,448,185)
        draw_wall(448,140,448,185)
        
        #D
        draw_wall(2,230,90,230)
        draw_wall(2,230,2,275)
        draw_wall(2,275,90,275)
        
        #E
        draw_wall(358,280,358,320)
        draw_wall(358,320,448,320)
        draw_wall(448,280,448,320)
        
        #F
        draw_wall(715,95,800,95)
        draw_wall(800,95,800,140)
        draw_wall(715,140,800,140)
        
        #G
        draw_wall(715,185,800,185)
        draw_wall(800,185,800,230)
        draw_wall(715,230,800,230)

        draw_obsatcle(180, 45, 180, 95)
        draw_obsatcle(265, 45, 265, 95)
        draw_obsatcle(180,45,265,45)
        draw_obsatcle(180,95,265,95)
        
        draw_obsatcle(180, 140, 180, 185)
        draw_obsatcle(265, 140, 265, 185)
        draw_obsatcle(180,140,265,140)
        draw_obsatcle(180,185,265,185)
        
        draw_obsatcle(180, 230, 180, 275)
        draw_obsatcle(265, 230, 265, 275)
        draw_obsatcle(180,230,265,230)
        draw_obsatcle(180,275,265,275)
        
        draw_obsatcle(180,280,180,320)
        draw_obsatcle(265,280,265,320)
        draw_obsatcle(180,280,265,280)
        draw_obsatcle(180,320,265,320)
        
        draw_obsatcle(360, 1, 360, 45)
        draw_obsatcle(445, 1, 445, 45)
        draw_obsatcle(360,2,445,2)
        draw_obsatcle(360,45,445,45)
        
        draw_obsatcle(360, 185, 360, 230)
        draw_obsatcle(445, 185, 445, 230)
        draw_obsatcle(360,230,445,230)
        
        draw_obsatcle(540, 95, 540, 185)
        draw_obsatcle(625, 95, 625, 185)
        draw_obsatcle(540,95,625,95)
        draw_obsatcle(540,185,625,185)
        
        draw_obsatcle(540, 235, 540, 280)
        draw_obsatcle(625, 235, 625, 280)
        draw_obsatcle(540,235,625,235)
        draw_obsatcle(540,280,625,280)
        
        
    def create_top_text_label(self):
        label_top_text = "Package is on the way"
        label_top = tk.Label(self.top_frame, text=label_top_text, bg='#7F7B82', fg="#FFFFFF",
                             font=('Ubuntu', 32, "bold"))
        label_top.place(x=46, y=23)



    