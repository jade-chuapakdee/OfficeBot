import tkinter as tk

from StartPage import StartPage
from pageOne import PageOne
from pageTwo import PageTwo
from pageThree import PageThree

pages = {
    "StartPage": StartPage, 
    "PageOne": PageOne, 
    "PageTwo": PageTwo,
    "PageThree": PageThree
}

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Officebot")
        self.geometry("750x500")
        self.resizable(False, False)
        self._frame = None
        self.switch_frame("StartPage")
        self.shared_reason = tk.StringVar()

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master = self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()