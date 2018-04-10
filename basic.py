import Tkinter as tk
import flip

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        #flip button
        self.flipButton = tk.Button(self, text="Flip Them Bitches",
            command = lambda: flip.doAll("flip"), height = 5, width = 15)
        self.flipButton.grid(row=0, column=1)

        #fix button
        self.fixButton = tk.Button(self, text="OH FUCK FIX IT",
            command = lambda: flip.doAll("fix"), height = 5, width = 15)
        self.fixButton.grid(row=1, column=1)

        #quit button
        self.quitButton = tk.Button(self, text="Quit",
            command=self.quit)
        self.quitButton.grid(row=2, column=1)


app = Application()
app.master.title("GUI OF DOOM")
app.master.geometry('100x200')
app.mainloop()
