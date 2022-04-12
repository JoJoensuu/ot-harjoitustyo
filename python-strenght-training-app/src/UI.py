from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="BUTTON")

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W))

        button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure(1, weight=1)


window = Tk()
window.title("TkInter example")
ui = UI(window)
ui.start()
window.mainloop()