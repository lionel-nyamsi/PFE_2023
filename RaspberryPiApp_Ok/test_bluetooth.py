import socket

"""hostname = socket.gethostname()
ip_address = socket.gethostbyname_ex(hostname)
for adr in ip_address[2] :
    if '-' in adr :
        print("Adresse MAC : ", adr)
        break"""

adapter_addr = "88:83:5d:fd:7a:af"
port = 3  # Normal port for rfcomm?
buf_size = 1024

print('Debut!')
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((adapter_addr, port))
print('Done!')
s.listen(1)
try:
    print('Listening for connection...')
    client, address = s.accept()
    print(f'Connected to {address}')

    while True:
        data = client.recv(buf_size)
        if data:
            print(data)
except Exception as e:
    print(f'Something went wrong: {e}')
finally:
    client.close()
    s.close()

print("Fin !")