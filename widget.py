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
        #self.root.eval('tk::PlaceWindow . center')
        #self.root.geometry()
        self.root.geometry('+1+'+str(self.hs))
        
        # wysunięcie aplikacji na samą górę
        self.root.lift()
        self.root.wm_attributes("-topmost",True)
        # dodanie podpisu na górze okna
        self.label = Label(
            text="Wprowadź podpis:",
            font=("Calibri bold",10),
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

        # dodanie przycisku Zapisz
        self.canvas.bind("<B1-Motion>")
        self.buttonSave = Button(
            text="Potwierdź",
            font=("Calibri bold",24),
            background = background,
            foreground= foreground)
        self.buttonSave.pack()

        self.space = Label(
            text="---",
            font=("Calibri bold",13),
            background = background,
            foreground = foreground)
        self.space.pack()
                
        # dodanie przycisku Anuluj
        self.canvas.bind("<B1-Motion>")
        self.buttonCancel = Button(
            text="Anuluj",
            font=("Calibri bold",11),
            background = background,
            foreground= foreground,
            command=self.root.quit)
        self.buttonCancel.pack()

    def _runTk(self):
        self.root.mainloop()


    
    def _configTk(self):
        pass

    def _getWindow(self):
        return self.root

# funkcja centrująca okno 
# from: https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
def _centerWindow(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# pętla główna aplikacji
if __name__ == "__main__":
    window = _MainTk()
    _centerWindow(window._getWindow())
    window._runTk()