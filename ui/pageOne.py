import tkinter as tk
from PIL import Image, ImageTk
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(fill= "both", expand=True)
        
        self.canvas = tk.Canvas(self, width=750, height=500)
        self.canvas.pack()

        img = Image.open("ui/image/newgraph.png")
        self.background_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0,0, anchor=tk.NW, image=self.background_image)
        self.canvas.create_oval(50, 50, 150, 150, width=1, outline="green")
        

if __name__ == "__main__":
    app = PageOne()
    app.mainloop()