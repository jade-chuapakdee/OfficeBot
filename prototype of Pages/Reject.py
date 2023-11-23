import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x506")
        self.configure(bg="#E5D0CC")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(bg="#E5D0CC")
        
        canvas = tk.Canvas(self, bg="#E5D0CC", height=506, width=900, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        canvas.create_rectangle(
            7.0,
            0.0,
            770.0,
            100.0,
            fill="#7F7B82",
            outline=""
        )

        canvas.create_text(
            232.0,
            169.0,
            anchor="nw",
            text="Your Package was REJECTED",
            fill="#444554",
            font=("RobotoSlab Bold", 30 * -1)
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            914.0,
            100.0,
            fill="#7F7B82",
            outline=""
        )

        canvas.create_text(
            46.0,
            24.0,
            anchor="nw",
            text="Package Rejected",
            fill="#FFFFFF",
            font=("Ubuntu Bold", 40 * -1)
        )

        canvas.create_text(
            304.0,
            250.0,
            anchor="nw",
            text="Reason: ",
            fill="#444554",
            font=("Ubuntu Bold", 30 * -1)
        )

        canvas.create_text(
            426.0,
            250.0,
            anchor="nw",
            text="Wrong Table",
            fill="#444554",
            font=("Ubuntu Bold", 30 * -1)
        )

        # Use a normal button instead of an image button
        button_1 = tk.Button(
            self,
            text="Click me",
            command=lambda: print("button_1 clicked"),
            width=10,
            height=1,
            bg="#83c6d2",
            fg="black",
            font=("Helvetica", 16, "bold"),
            borderwidth=1
        )
        button_1.place(x=360.0, y=391.0, width=180.0, height=50.0)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
