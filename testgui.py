from logging import root
import tkinter as tk
import tkinter.font as tkFont

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.url = 'http://www.isomizer.com'
        self.source_url = 'https://github.com/crydonry/onmyoji_bot'
        self.master = master
        self.master.iconbitmap('img/icon/OnmyojiBot.ico')

        self.master.geometry("800x600")

        self.pack()

        # Create title
        self.create_title()

        # Create a menu bar
        self.create_menubar()
    def create_title(self):
         # title
        tk.Label(self.master, text='OnmyojiBot By Isomizer',
                 font='Helvetica 20 bold').pack(anchor=tk.W)
        tk.Label(
            self.master, text=self.url).pack(anchor=tk.W)

        # home page
        self.main_frame1 = tk.Frame(self.master)
        self.main_frame2 = tk.Frame(self.master)
        self.main_frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.main_frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_menubar(self):
        '''
        Create a menu bar
        '''
        menubar = tk.Menu(self.master)

        # Create a menu item
        menu1 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="file")
        menu1.add_command(label='start up')
        menu1.add_command(label='drop out')

        # advanced options
        menu2 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="advanced")
        menu2.add_command(label='Custom delay')

        # help
        menu3 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='help')
        menu3.add_command(label='info')
        menu3.add_command(label='Instructions for use')
        menu3.add_separator()
        menu3.add_command(label='Donation')

        # Set
        self.master.config(menu=menubar)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

