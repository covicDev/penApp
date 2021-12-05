from tkinter import *

#globals
width = 600
height = 200
background = "#1B1E26"
foreground = "#FFE222"
white = "#FFFFFF"

class _MainTk:
    def __init__(self):
        # Stworzenie podstawowego okna
        self.root = Tk()
        # pobranie wartości pulpitu
        self.ws = self.root.winfo_screenwidth()
        self.hs = self.root.winfo_screenheight()
        # nadanie nazwy aplikacji
        self.root.title("Aplikacja do podpisu")
        # zablokowanie możliwości zmiany rozmiaru okna
        self.root.resizable( width = False, height = False )
        # nadanie koloru okna
        self.root.config(bg=background)
        # usunięcie górnego paska okna
        self.root.overrideredirect(True)
        # wysunięcie aplikacji na samą górę
        self.root.lift()
        self.root.wm_attributes("-topmost",True)
        # dodanie podpisu na górze okna
        self.label = Label(
            text="Wprowadź podpis:",
            font=("Calibri bold",9),
            background = background,
            foreground = foreground)
        self.label.pack()
        # dodanie canvasu na podpis
        self.canvas = Canvas(
            self.root,
            width=width,
            height=height,
            bg= white
        )
        self.canvas.pack()
        # dodanie przycisku zapisz
        self.canvas.bind("<B1-Motion>")
        self.button = Button(text="Zapisz")
        self.button.pack()

    def _runTk(self):
        self.root.mainloop()

    def _configTk(self):
        pass

# pętla główna aplikacji
if __name__ == "__main__":
    window = _MainTk()
    window._runTk()