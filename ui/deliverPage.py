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
            
        def draw_obsatcle(x,y):
            self.canvas.itemconfig(f"t_{x}_{y}", fill="red")
            self.canvas.itemconfig(f"b_{x}_{y}" , fill="red")
            self.canvas.itemconfig(f"l_{x}_{y}", fill="red")
            self.canvas.itemconfig(f"r_{x}_{y}", fill="red")
            
            
        def draw_cell(x1,y1,x2,y2,i,j):
            self.canvas.create_line(x1, y1, x2, y2, fill="#7F7B82", width=2, tags=f"t_{i}_{j}")
            self.canvas.create_line(x1, y1+52, x2, y2+52, fill="#7F7B82", width=2, tags=f"b_{i}_{j}")
            self.canvas.create_line(x1, y1, x2-78, y2+52, fill="#7F7B82", width=2, tags=f"l_{i}_{j}")
            self.canvas.create_line(x1+78, y1, x2, y2+52, fill="#7F7B82", width=2, tags=f"r_{i}_{j}")
            

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
        
            
        draw_cell(5, 5, 83 , 5, 0, 0)
        draw_cell(5, 58, 83 , 58, 0, 1)
        draw_cell(5, 111, 83 , 111, 0, 2)
        draw_cell(5, 164, 83 , 164, 0, 3)
        draw_cell(5, 217, 83 , 217, 0, 4)
        draw_cell(5, 270, 83 , 270, 0, 5)
        draw_cell(84, 5, 162 , 5, 1, 0)
        draw_cell(84, 58, 162 , 58, 1, 1)
        draw_cell(84, 111, 162 , 111, 1, 2)
        draw_cell(84, 164, 162 , 164, 1, 3)
        draw_cell(84, 217, 162 , 217, 1, 4)
        draw_cell(84, 270, 162 , 270, 1, 5)
        draw_cell(163, 5, 241 , 5, 2, 0)
        draw_cell(163, 58, 241 , 58, 2, 1)
        draw_cell(163, 111, 241 , 111, 2, 2)
        draw_cell(163, 164, 241 , 164, 2, 3)
        draw_cell(163, 217, 241 , 217, 2, 4)
        draw_cell(163, 270, 241 , 270, 2, 5)
        draw_cell(242, 5, 320 , 5, 3, 0)
        draw_cell(242, 58, 320 , 58, 3, 1)
        draw_cell(242, 111, 320 , 111, 3, 2)
        draw_cell(242, 164, 320 , 164, 3, 3)
        draw_cell(242, 217, 320 , 217, 3, 4)
        draw_cell(242, 270, 320 , 270, 3, 5)
        draw_cell(321, 5, 399 , 5, 4, 0)
        draw_cell(321, 58, 399 , 58, 4, 1)
        draw_cell(321, 111, 399 , 111, 4, 2)
        draw_cell(321, 164, 399 , 164, 4, 3)
        draw_cell(321, 217, 399 , 217, 4, 4)
        draw_cell(321, 270, 399 , 270, 4, 5)
        draw_cell(400, 5, 478 , 5, 5, 0)
        draw_cell(400, 58, 478 , 58, 5, 1)
        draw_cell(400, 111, 478 , 111, 5, 2)
        draw_cell(400, 164, 478 , 164, 5, 3)
        draw_cell(400, 217, 478 , 217, 5, 4)
        draw_cell(400, 270, 478 , 270, 5, 5)
        draw_cell(479, 5, 557 , 5, 6, 0)
        draw_cell(479, 58, 557 , 58, 6, 1)
        draw_cell(479, 111, 557 , 111, 6, 2)
        draw_cell(479, 164, 557 , 164, 6, 3)
        draw_cell(479, 217, 557 , 217, 6, 4)
        draw_cell(479, 270, 557 , 270, 6, 5)
        draw_cell(558, 5, 636 , 5, 7, 0)
        draw_cell(558, 58, 636 , 58, 7, 1)
        draw_cell(558, 111, 636 , 111, 7, 2)
        draw_cell(558, 164, 636 , 164, 7, 3)
        draw_cell(558, 217, 636 , 217, 7, 4)
        draw_cell(558, 270, 636 , 270, 7, 5)
        draw_cell(637, 5, 715 , 5, 8, 0)
        draw_cell(637, 58, 715 , 58, 8, 1)
        draw_cell(637, 111, 715 , 111, 8, 2)
        draw_cell(637, 164, 715 , 164, 8, 3)
        draw_cell(637, 217, 715 , 217, 8, 4)
        draw_cell(637, 270, 715 , 270, 8, 5)
        draw_cell(716, 5, 794 , 5, 9, 0)
        draw_cell(716, 58, 794 , 58, 9, 1)
        draw_cell(716, 111, 794 , 111, 9, 2)
        draw_cell(716, 164, 794 , 164, 9, 3)
        draw_cell(716, 217, 794 , 217, 9, 4)
        draw_cell(716, 270, 794 , 270, 9, 5)
        
        draw_obsatcle(2,0)
        draw_obsatcle(2,2)
        draw_obsatcle(2,4)
        draw_obsatcle(2,5)
        draw_obsatcle(4,3)
        draw_obsatcle(6,1)
        draw_obsatcle(6,2)
        draw_obsatcle(6,4)
        draw_obsatcle(7,2)
        draw_obsatcle(9,4)
        
        obasacle = ["2,0","2,2","2,4","2,5","4,3","6,1","6,2","6,4","7,2","9,4"]
                
        
        
        
        #text in cells
        self.canvas.create_text(360, 140, text="C", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 140, text="B", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 30, text="A", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(40, 240, text="D", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(360, 300, text="E", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(750, 90, text="F", font=("Helvetica", 16), fill="blue")
        self.canvas.create_text(750, 190, text="G", font=("Helvetica", 16), fill="blue")
        
        
    def create_top_text_label(self):
        label_top_text = "Package is on the way"
        label_top = tk.Label(self.top_frame, text=label_top_text, bg='#7F7B82', fg="#FFFFFF",
                             font=('Ubuntu', 32, "bold"))
        label_top.place(x=46, y=23)



    