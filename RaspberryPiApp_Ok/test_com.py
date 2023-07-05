import socket

ADRESSE_MAC = '88:83:5d:fd:7a:af'
PORT = 1
DATA_SIZE = 1024

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect((ADRESSE_MAC, PORT))

try:
    while True:
        message = input("Entrer un message : ")
        client.send(message.encode('utf-8'))
        data = client.recv(DATA_SIZE)
        if not data:
            break
        print("Message : {}".format(data.decode('utf-8')))

except OSError as error:
    print("ERROR : ", error)

finally:
    client.close()