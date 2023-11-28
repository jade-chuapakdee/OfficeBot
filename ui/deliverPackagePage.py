import tkinter as tk
from PIL import Image, ImageTk
import ast

class DeliverPackage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        self.configure(bg = "#E5D0CC")
        self.master = master

        self.canvas = tk.Canvas(self, width=740, height=421)
        self.canvas.pack()
        self.canvas.place(x=0, y=80)
        
        self.top_frame = tk.Frame(bg="#7F7B82", width=900, height=100)   
        self.top_frame.place(x=0, y=0)
       
        self.create_top_text_label()
        
        self.create_path_details_label()
        
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
        blue_label = tk.Label(self, text="= paths",bg='#E5D0CC',fg="#444554" , font=('Ubuntu',12))
        red_label = tk.Label(self, text="= Destination",bg='#E5D0CC',fg="#444554" , font=('Ubuntu',12))
        
        green_label.place(x=795, y=335)
        blue_label.place(x=795, y=385)
        red_label.place(x=795, y=435)
        
        img = Image.open("ui/image/graph_750x421.png")
        self.master = master
        

        img = Image.open("ui/image/graph_750x421.png")
        self.background_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0,0, anchor=tk.NW, image=self.background_image)

        self.vertexes = {
            "a1" : [41.5, 210],
            "a2" : [100, 147],
            "a3" : [102, 256],
            "a4" : [186, 147],
            "a5" : [185, 257],
            "b1" : [287, 147],
            "b2" : [287, 254],
            "b3" : [374, 147],
            "b4" : [374, 254],
            "b5" : [460, 147],
            "c1" : [460, 254],
            "c2" : [536, 147],
            "c3" : [536, 254],
            "c4" : [621, 147],
            "c5" : [616, 253]
        }

        self.edges = {
            "a1,a2" : [55, 202, 88, 164],
            "a2,a4" : [119, 148, 167, 148],
            "a4,a2" : [
                [186,130, 186,106], 
                [186,106, 100,106], 
                [100,106, 100,130],
            ],
            "a1,a3" : [53,226,83,247],
            "a3,a4" : [100,239,173,161],
            "a4,a5" : [186,167,186,237],
            "a5,a3" : [ 167, 258, 123, 258],
            "a5,b1" : [ 202, 251, 275, 162,],
            "a5,b2" : [ 203, 255, 268, 255,],
            "b1,a5" : [ 270, 154, 197, 242,],
            "b1,b3" : [ 305, 147, 356, 147,],
            "b2,b1" : [ 287, 235, 287, 167,],
            "b2,b3" : [ 306, 248, 362, 162,],
            "b3,b4" : [ 375, 165, 375, 236,],
            "b4,b5" : [ 389, 241, 446, 161,],
            "b4,c1" : [ 395, 254, 441, 254,],
            "b5,b4" : [ 441, 152, 382, 237,],
            "b5,c2" : [ 480, 148, 516, 148,],
            "c1,b5" : [ 461, 237, 461, 167,],
            "c1,c2" : [ 471, 241, 524, 162,],
            "c2,c3" : [ 537, 166, 537, 235,],
            "c2,c4" : [ 556, 149, 600, 149,],
            "c3,b4" : [
                [ 536, 272, 537, 300,],
                [ 537, 300, 375, 300,],
                [ 375, 300, 374, 274,],
            ],
            "c3,c5" : [ 555, 254, 598, 254,],
            "c4,c1" : [
                [ 639, 150, 661, 150,],
                [ 661, 150, 661, 360,],
                [ 661, 360, 460, 359,],
                [ 461, 359, 461, 273,],
            ],
            "c4,c5" : [ 618, 166, 619, 234,],
            "c5,a1" : [
                [ 618, 273, 618, 346,],
                [ 618, 346, 42, 346,],
                [ 42, 346, 42, 232,],
            ],
        }

        self.start_draw_path()


    def start_draw_path(self):
        path = (list(ast.literal_eval(self.master.shared_path.get())))
        self.draw_path(path, self.vertexes, self.edges, 0) 
        

    def draw_path(self, path, vertexes, edges, index):
        if index >= len(path) - 1:
            # Draw the last circle (red) when we reach the end of the path
            v = path[-1]
            vertex_x = vertexes[v][0]
            vertex_y = vertexes[v][1]
            outline = 'red'
            self.create_circle(vertex_x, vertex_y, outline)
            return

        v = path[index]
        vertex_x = vertexes[v][0]
        vertex_y = vertexes[v][1]
        if v == path[0]:
            outline = 'green'
        else:
            outline = '#4cd6f1'
        self.create_circle(vertex_x, vertex_y, outline)

        e = f'{path[index]},{path[index + 1]}'
        coordinates = edges[e]
        if type(coordinates[0]) == type(1):
            x1, y1, x2, y2 = coordinates
            self.draw_line_with_delay(x1, y1, x2, y2, index, path, vertexes, edges)
        else:
            for coor in coordinates:
                x1, y1, x2, y2 = coor
                if coordinates[-1] != coor:
                    self.draw_line_with_delay(x1, y1, x2, y2, index, path, vertexes, edges, False)
                else:
                    self.draw_line_with_delay(x1, y1, x2, y2, index, path, vertexes, edges, True)

    def draw_line_with_delay(self, x1, y1, x2, y2, index, path, vertexes, edges, has_arrow=True):
        width = 3
        fill = 'purple'
        arrow = tk.LAST
        arrowshape = (4, 4, 6)
        delay = 500  # Adjust the delay as needed

        if has_arrow:
            self.canvas.create_line(x1, y1, x1, y1, width=width, fill=fill, arrow=arrow, arrowshape=arrowshape)
        else:
            self.canvas.create_line(x1, y1, x1, y1, width=width, fill=fill)

        self.after(delay, self.draw_line, x1, y1, x2, y2, has_arrow, index, path, vertexes, edges)

    def draw_line(self, x1, y1, x2, y2, has_arrow, index, path, vertexes, edges):
        width = 3
        fill = 'purple'
        arrow = tk.LAST
        arrowshape = (4, 4, 6)

        if has_arrow:
            self.canvas.create_line(x1, y1, x2, y2, width=width, fill=fill, arrow=arrow, arrowshape=arrowshape)
        else:
            self.canvas.create_line(x1, y1, x2, y2, width=width, fill=fill)

        self.draw_path(path, vertexes, edges, index + 1)

    def create_circle(self, origin_x, origin_y, outline):
        circle_outline_width = 4
        circle_outline_color = outline
        length = 35

        radius = length / 2

        top_left_x = origin_x - radius
        top_left_y = origin_y - radius

        bottom_rigt_x = origin_x + radius
        bottom_rigt_y = origin_y + radius

        self.canvas.create_oval(top_left_x, top_left_y, bottom_rigt_x, bottom_rigt_y,
                                 width=circle_outline_width,
                                 outline=circle_outline_color)
        
        if outline=='red':
            self.change_page_to()
    
    def change_page_to(self):
        self.after(5000, lambda: self.master.switch_frame("ReachedPage"))

    def create_line(self, x1, y1, x2, y2, has_arrow = True):
        width = 3
        fill = 'purple'
        arrow = tk.LAST
        arrowshape = (4,4,6)
        if has_arrow:
            self.canvas.create_line(x1, y1, x2, y2, width=width, fill=fill, arrow=arrow, arrowshape=arrowshape)
        else:
            self.canvas.create_line(x1, y1, x2, y2, width=width, fill=fill)

    def create_top_text_label(self):
        label_top_text = "Package is on the way"
        label_top = tk.Label(self.top_frame, text= label_top_text,bg='#7F7B82' , fg = "#FFFFFF", font=('Ubuntu',32, "bold"))
        label_top.place(x = 46, y = 23)

    def create_path_details_label(self):
        label1_text = "Destination: " + self.master.shared_destination.get()
        label1 = tk.Label(self, text= label1_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label1.place(x = 755, y = 150)
        
        label2_text = "Source: " + self.master.shared_from.get()
        label2 = tk.Label(self, text= label2_text,bg='#E5D0CC',fg="#444554" , font=('Ubuntu',14))
        label2.place(x = 755, y = 200)
        
        
        

if __name__ == "__main__":
    app = DeliverPackage()
    app.mainloop()

