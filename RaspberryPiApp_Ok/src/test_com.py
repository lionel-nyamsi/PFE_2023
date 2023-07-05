import socket

ADRESSE_MAC = "88:83:5d:fd:7a:af"
PORT = 1
DATA_SIZE = 1024

server =  socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((ADRESSE_MAC, PORT))
server.listen(1)

try:
    print('Ecoute des connexions...')
    client, address = server.accept()
    print("Connectee a {}".format(address))

    while True:
        data = client.recv(DATA_SIZE)
        if not data:
            break
        print("Message : {}".format(data.decode('utf-8')))
        message = input("Entrer un message : ")
        client.send(message.encode('utf-8'))
except OSError as error:
    print("ERROR : ", error)

finally:
    client.close()
    server.close()