# Implementacja serwera www:

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
# ustalenie portu komunikacji
PORT = 9000

class _myRequestHandler(BaseHTTPRequestHandler):
    # metoda dziedziczona i przeciążona z klasy BaseHTTPRequestHandler (ładowana w momencie request'a get)
    def do_GET(self):
        # sprawdzenie ścieżki adresu
        if self.path.endswith('/zlecenie'):
            self._stronaZlecenie()
        else:
            self._stronaStartowa()
    
    # wyświetlenie strony zlecenia
    def _stronaZlecenie(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        os.system('notepad')
        self.wfile.write(self.path[1:].encode())

    # wyświetlenie komunikatu strony startowej
    def _stronaStartowa(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Aplikacja do generowania sygnatur.'.encode())

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