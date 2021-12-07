# Implementacja serwera www:

from http.server import HTTPServer, BaseHTTPRequestHandler

# ustalenie portu komunikacji
PORT = 9000

class _myRequestHandler(BaseHTTPRequestHandler):
    # metoda dziedziczona i przeciążona z klasy BaseHTTPRequestHandler (ładowana w momencie request'a get)
    def do_GET(self):
        # prosta odpowiedź 200 na każde zapytanie www
        self.send_response(200)
        # rodzaj treści odpowiedzi (nagłówek)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # pokazuje ściękę www np. localhost:9000/test -> pokaże: test
        self.wfile.write(self.path[1:].encode())
    
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