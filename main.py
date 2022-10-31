#
# TCP Server efter bogen + threading
#

from socket import *
from threading import *
# konstant
serverPort = 12001


# metode til at håndtere een client
def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()     # modetager op til 2048 tegn i en sætning og laver byte om til tekst(decode)
    upperSentence = sentence.upper()
    clientSocket.send(upperSentence.encode())       # sender tekst tilbage til clienten og laver tekst om til byte (encode)
    clientSocket.close()                            # lukker forbindelse til klienten


#
# Main program
#
# opretter server objekt
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))              # lader serveren køre på denne maskiner og på port = serverPort
serverSocket.listen(1)                          # sætter serverne reelt til at starte alias lytte efter clienter
print('The server is up and runing on port', serverSocket)

#server loop
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Forbundet til en Client fra adressen', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()

