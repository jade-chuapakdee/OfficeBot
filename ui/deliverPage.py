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
            
        def draw_paths(paths):
            for i, path in enumerate(paths):
                x, y = path
                if i == 0:
                    # Draw the first path in a different color (e.g., blue)
                    draw_path(x, y, color="blue")
                elif i == len(paths) - 1:
                    # Draw the last path in a different color (e.g., red)
                    draw_path(x, y, color="blue")
                else:
                    # Draw other paths in the default color
                    draw_path(x, y, color="green")
            
        def draw_path(x,y, color):
            self.canvas.itemconfig(f"t_{x}_{y}", fill=color)
            
        def draw_wall(x1,y1,x2,y2):
            self.canvas.create_line(x1,y1,x2,y2, width=3, fill="red" )
            self.canvas.create_line(x1,y1+52,x2,y2+52, width=3, fill="red" )
            self.canvas.create_line(x1,y1,x2-78,y2+52, width=3, fill="red" )
        
        def draw_wall2(x1,y1,x2,y2):
            self.canvas.create_line(x1,y1+52,x2,y2+52, width=3, fill="red" )
            self.canvas.create_line(x1,y1,x2-78,y2+52, width=3, fill="red" )
            self.canvas.create_line(x1+78,y1,x2,y2+52, width=3, fill="red" )
            
        def draw_wall3(x1,y1,x2,y2):
            self.canvas.create_line(x1,y1,x2,y2, width=3, fill="red" )
            self.canvas.create_line(x1,y1+52,x2,y2+52, width=3, fill="red" )
            self.canvas.create_line(x1+78,y1,x2,y2+52, width=3, fill="red" )
            
        
        
        def draw_obsatcle(x,y):
            self.canvas.itemconfig(f"t_{x}_{y}", fill="purple")
            
        
        def draw_cell(x1,y1,i,j):
            self.canvas.create_rectangle(x1,y1,x1+78,y1+52, width=2, tags=f"t_{i}_{j}")
            

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
        
            
        draw_cell(5, 5, 0, 0)
        draw_cell(5, 58, 0, 1)
        draw_cell(5, 111, 0, 2)
        draw_cell(5, 164, 0, 3)
        draw_cell(5, 217, 0, 4)
        draw_cell(5, 270, 0, 5)
        draw_cell(84, 5, 1, 0)
        draw_cell(84, 58, 1, 1)
        draw_cell(84, 111, 1, 2)
        draw_cell(84, 164, 1, 3)
        draw_cell(84, 217, 1, 4)
        draw_cell(84, 270, 1, 5)
        draw_cell(163, 5, 2, 0)
        draw_cell(163, 58, 2, 1)
        draw_cell(163, 111, 2, 2)
        draw_cell(163, 164, 2, 3)
        draw_cell(163, 217, 2, 4)
        draw_cell(163, 270, 2, 5)
        draw_cell(242, 5, 3, 0)
        draw_cell(242, 58, 3, 1)
        draw_cell(242, 111, 3, 2)
        draw_cell(242, 164, 3, 3)
        draw_cell(242, 217, 3, 4)
        draw_cell(242, 270, 3, 5)
        draw_cell(321, 5, 4, 0)
        draw_cell(321, 58, 4, 1)
        draw_cell(321, 111, 4, 2)
        draw_cell(321, 164, 4, 3)
        draw_cell(321, 217, 4, 4)
        draw_cell(321, 270, 4, 5)
        draw_cell(400, 5, 5, 0)
        draw_cell(400, 58, 5, 1)
        draw_cell(400, 111, 5, 2)
        draw_cell(400, 164, 5, 3)
        draw_cell(400, 217, 5, 4)
        draw_cell(400, 270, 5, 5)
        draw_cell(479, 5, 6, 0)
        draw_cell(479, 58, 6, 1)
        draw_cell(479, 111, 6, 2)
        draw_cell(479, 164, 6, 3)
        draw_cell(479, 217, 6, 4)
        draw_cell(479, 270, 6, 5)
        draw_cell(558, 5,7, 0)
        draw_cell(558, 58, 7, 1)
        draw_cell(558, 111, 7, 2)
        draw_cell(558, 164, 7, 3)
        draw_cell(558, 217, 7, 4)
        draw_cell(558, 270, 7, 5)
        draw_cell(637, 5, 8, 0)
        draw_cell(637, 58, 8, 1)
        draw_cell(637, 111, 8, 2)
        draw_cell(637, 164, 8, 3)
        draw_cell(637, 217, 8, 4)
        draw_cell(637, 270, 8, 5)
        draw_cell(716, 5, 9, 0)
        draw_cell(716, 58, 9, 1)
        draw_cell(716, 111, 9, 2)
        draw_cell(716, 164, 9, 3)
        draw_cell(716, 217, 9, 4)
        draw_cell(716, 270, 9, 5)
        
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
        
        draw_wall(5,5,83,5)
        draw_wall(5,110,83,110)
        draw_wall(5,216,83,216)
        
        draw_wall2(320,110,398,110)
        draw_wall2(320,270,398,270)
        
        draw_wall3(715,60,793,60)
        draw_wall3(715,164,793,164)
        
        # paths_array = [[1, 0], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [9, 1]]

    
        # draw_paths(paths_array)
        
        self.obstacle = ["2,0","2,2","2,4","2,5","4,3","6,1","6,2","6,4","7,2","9,4"]
        master.shared_ob.set(self.obstacle)
        
        
               
        #text in cells
        self.canvas.create_text(360, 140, text="C", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(40, 140, text="B", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(40, 30, text="A", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(40, 240, text="D", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(360, 300, text="E", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(750, 90, text="F", font=("Helvetica", 16), fill="black")
        self.canvas.create_text(750, 190, text="G", font=("Helvetica", 16), fill="black")
        
        
    def create_top_text_label(self):
        label_top_text = "Package is on the way"
        label_top = tk.Label(self.top_frame, text=label_top_text, bg='#7F7B82', fg="#FFFFFF",
                             font=('Ubuntu', 32, "bold"))
        label_top.place(x=46, y=23)



    