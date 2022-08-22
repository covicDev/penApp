# penApp
EN |<br>
Pencil Signature Application with web access with standalone http server.

PL |<br>
Aplikacja do zbierania podpisów z dostępem web i samodzielnym serwerem http.
<br>
Instrukcja:<br>
1.  Uruchom aplikacje server.exe <br>
Port nasłuchiwania <b>9000</b>.<br>
Komunikacja typu GET.<br>
Stała odpowiedź serwera ze statusem 200.<br>
2. Obsługuj serwer za pomocą komend: <br> 
[nazwaSerwera]:9000/<b>zlecenie</b> - wprowadza żądanie nowego podpisu. <br>
[nazwaSerwera]:9000/<b>zamknijserwer</b> - wprowadza żądanie zamknięcia serwera. <br>
[nazwaSerwera]:9000/<b>image.png</b> - [.png] wprowadza żądanie wyświetlenia obaru .png.<br>
gdzie [nazwaSerwera] to np. localhost albo 127.0.0.1
3. Komenda /<b>zlecenie</b> wywołuje okno programu:
![image](https://user-images.githubusercontent.com/80823913/185862422-007618ec-b564-4f5b-96f2-3bb8244d5bd6.png)<br>
Po wpisaniu podpisu i naciśnięciu przycisku "Potwierdź" następuje przekierowanie na wskazaną na stronę http.

<b>Poniżej przykład użycia</b>:
![OZNeZ3mUMv](https://user-images.githubusercontent.com/80823913/185883683-63f50075-bc2f-4c00-823a-de0dd3783336.gif)
