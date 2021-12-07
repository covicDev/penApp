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
        # treść odpowiedzi (html)
        output = 'Hello World!'
        # wysłanie odpowiedzi
        self.wfile.write(output.encode())
    
# pętla główna aplikacji
if __name__ == "__main__":
    # deklaracja servera na podstawie własnej klasy
    server = HTTPServer(('',PORT),_myRequestHandler)
    # tryb pracy serwera
    server.serve_forever()
