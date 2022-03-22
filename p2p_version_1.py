import socket
import os

#Functions or Definations here
def Recieve():
    # myHostName = socket.gethostname()
    # SERVER_HOST = socket.gethostbyname(myHostName)
    SERVER_HOST = "192.168.0.107"

    SERVER_PORT = 5001

    s = socket.socket()


    s.bind((SERVER_HOST, SERVER_PORT))


    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


    client_socket, address = s.accept() 

    print(f"[+] {address} is connected.")

    data = client_socket.recv(1024).decode()
    print(data)
    while True:
        if data.lower()!="end":
            print(data)
            data = client_socket.recv(1024).decode()
        else:
            s.close()
            break


def Send():
        host = input("Enter receiver ip:")
        port = 5001
        
        s = socket.socket()

        print(f"[+] Connecting to {host}:{port}")
        s.connect((host, port))
        print("[+] Connected.")
        print("host is",host)

        data = input("YOU: ")
        while True:
            if data.lower()!="end":
                s.send(bytes(data,"utf-8"))
                data = input("YOU: ")
            else:
                s.send(b'end')
                s.close()
                break
def process_input(input_data):
    if data.lower() == "recieve":
            Recieve()
    if data.lower() == "send":
        Send()


if __name__=="__main__":
    # while True:
    data=input("Send Or Recieve")
    if data.lower() in ["send","recieve"]:
        process_input(data)
    else:
        print("INVALID COMMAND")
    # data = send|receive
        

