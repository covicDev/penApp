# Implementacja serwera www:

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys 
from os import curdir

# ustalenie portu komunikacji
PORT = 9000

class _myRequestHandler(BaseHTTPRequestHandler):
    # metoda dziedziczona i przeciążona z klasy BaseHTTPRequestHandler (ładowana w momencie request'a get)
    def do_GET(self):
        # sprawdzenie ścieżki adresu
        if self.path.endswith('/zlecenie'): # wywołanie żądania nowego podpisu
            self._stronaZlecenie()
        elif self.path.endswith('/zamknijserwer'): # wywołanie żądania zamknięcia serwera
            self._stronaZamknijSerwer()
        elif self.path.endswith('.png'): # wywołanie żądania wyświetlenia obrazu z rozszerzeniem .png
            self._stronaObraz()
        else:
            self._stronaStartowa()

    # wyświetlenie strony zlecenia
    def _stronaZlecenie(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        os.system('widget.exe')
        output = ''
        output += '<html><body>'
        output += '<img src="image.png"/><br>Otrzymany podpis.'
        output += '</body></html>'
        self.wfile.write(output.encode())

    # wyświetlenie komunikatu strony startowej
    def _stronaStartowa(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Aplikacja do generowania sygnatur.'.encode())

    # wyświetlenie komunikatu i zgaszenie serwera (za pomocą przeglądarki)
    def _stronaZamknijSerwer(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Serwer zgaszony.'.encode())
        sys.exit()

    # wyświetlnie żądanego obrazu
    def _stronaObraz(self):
        f = open(curdir + '/' + self.path, 'rb')
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

# pętla główna aplikacji
if __name__ == "__main__":
    # deklaracja servera na podstawie własnej klasy
    # '' - localhost
    # PORT - 9000
    server = HTTPServer(('',PORT),_myRequestHandler)
    # tryb pracy serwera
    server.serve_forever()

# obługa dostępna przez przeglądarkę www
# obługa dostępna również przez telnet lub putty:
'''
--- przykładowa komunikacja (telnet) ---
telnet o localhost 900
<space>GET / HTTP/1.0<enter>
<enter>
(odpowiedź)
HTTP/1.0 200 Ok
content-type: text/html

Hello World!
/
'''