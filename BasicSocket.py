import socket, sys
import threading

def SendInput(pSock):
    while True:
        pSock.send((input()+'\n').encode())

def ReceiveData(pSock):
    recSize = 65536
    response = s.recv(recSize).decode("utf-8")
    while len(response) != 0:
        if response[len(response)-1] == '\n':
            response = response[0:len(response)-1]
        print(response)
        response = pSock.recv(recSize).decode("utf-8")


if len(sys.argv) != 3:
    print("Usage: python BasicSocket.py [hostname] [port]")
    sys.exit(0)

s = socket.socket()
s.connect((sys.argv[1],int(sys.argv[2])))

threads = []
threads.append(threading.Thread(target=SendInput,args=(s,)))
threads.append(threading.Thread(target=ReceiveData,args=(s,)))

threads[0].start()
threads[1].start()

threads[0].join()
threads[1].join()

s.close()
