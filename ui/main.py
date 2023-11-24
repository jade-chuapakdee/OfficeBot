import tkinter as tk

from StartPage import StartPage
from deliverPackagePage import DeliverPackage
from reachedPage import Reached
from pageReject import PageReject
from historyPage import HistoryPage
from returnPackagePage import ReturnPage

pages = {
    "StartPage": StartPage, 
    "DeliverPage": DeliverPackage, 
    "ReachedPage": Reached,
    "PageReject": PageReject,
    "HistoryPage": HistoryPage, 
    "ReturnPage": ReturnPage
}

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Officebot")
        self.geometry("900x506")
        self.resizable(False, False)
        self._frame = None
        self.switch_frame("StartPage")
        
        self.shared_reason = tk.StringVar()
        self.shared_destination = tk.StringVar()
        self.shared_from = tk.StringVar()
        self.shared_destination = tk.StringVar()
        self.shared_cost = tk.StringVar()
        self.shared_tray = tk.StringVar()
        self.shared_path = tk.StringVar()

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