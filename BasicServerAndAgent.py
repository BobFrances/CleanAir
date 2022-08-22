import socket
import threading
import time
import random

class Server:
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port

    def serverSend(self, c, data):
        message = bytes(('Here is a number: ' + str(data)), encoding='utf-8')
        c.send(message)
        
    def serverListen(self):
        s = socket.socket()
        s.bind((self.host, self.port))
        s.listen(2)
        while True:
            c, addr = s.accept()
            print("SERVER -- Connection from: " + str(addr))
            self.serverSend(c, str(random.randint(0, 100)))
            c.close()


class Agent:
    def __init__(self, serverHostName, serverPort):
        self.serverHostName = serverHostName
        self.serverPort = serverPort

    def agentSend(self):
        while True:
            s = socket.socket()
            s.connect((self.serverHostName, self.serverPort))
            self.agentListen(s)
            s.close()
            time.sleep(5)

    def agentListen(self, s):
        message = s.recv(1024)
        print("AGENT -- Recieved: " + str(message))


server = Server(12345)
agent = Agent(socket.gethostname(), 12345)

threads = []
threads.append(threading.Thread(target=server.serverListen,args=()))
threads.append(threading.Thread(target=agent.agentSend,args=()))

threads[0].start()
threads[1].start()

threads[0].join()
threads[1].join()
