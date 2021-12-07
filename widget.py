from tkinter import *
from PIL import ImageDraw

import PIL
import sys

#globals
width = 800
height = 300
background = "#1B1E26"
foreground = "#FFE222"
white = "#FFFFFF"
penColor = "#000000" # <todo> have some problems with that
penSize = 8
fileName = "image.png"

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

        '''
        # organizes widgets in blocks before placing them in the parent widget
        expand − When set to true, widget expands to fill any space not otherwise used in widget's parent.
        fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically).
        '''
        self.canvas.pack(expand=YES, fill=BOTH)

        # do Buttonów (Canvasa) przypiszę funkcję reagującą na zdarzenie <Button-1> czyli kliknięcie lewym przyciskiem myszy, następnie podaje funkcje
        self.canvas.bind("<B1-Motion>",paint)

        # dodanie przycisku Zapisz
        self.buttonSave = Button(
            text="Potwierdź",
            font=("Calibri bold",24),
            background = background,
            foreground= foreground,
            command=save)
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

    # metoda odpowiadająca za pętlę uruchomienia okna
    def _runTk(self):
        self.root.mainloop()

    # metoda do implementacji dla dodatkowych parametrów okna
    def _configTk(self,**arguments):
        pass
    
    # pobranie canvasa okna
    def _getCanvas(self):
        return self.canvas

    # pobranie widuku okna
    def _getWindow(self):
        return self.root

# funkcja reagująca na kliknięci lewym przyciskiem myszki w obszarze canvas | event: "<B1-Motion>"
def paint(event):
    x1 = (event.x - 1)
    x2 = (event.x + 1)
    y1 = (event.y - 1)
    y2 = (event.y + 1)
    globalCanvas.create_oval(x1,y1,x2,y2, fill=penColor, width=penSize-3)
    globalDraw.line([x1,y1,x2,y2], fill=penColor, width=penSize)

# funkcja zapisująca obraz
def save():
    globalImage.save(fileName)
    sys.exit()

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
    globalCanvas = window._getCanvas()
    # inicjalizacja przestrzeni obrazu podpisu
    globalImage = PIL.Image.new("RGB", (width, height), white)
    # inicjalizacja zapisu pikseli na obrazie
    globalDraw = ImageDraw.Draw(globalImage)
    window._runTk()