import json
import os.path
import pickle
import socket
import sqlite3

IP = "34.77.60.185"
PORT = 8080

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "site.db")
con = sqlite3.connect(db_path)
cursor = con.cursor()

def save_data(data, command):
    cursor.execute(f"INSERT INTO Info ({command}) VALUES ('{data}')")
    con.commit()

class Client:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.command = ""
        self.data = ""

    def send_data(self):
        self.command = input("Enter 'time', 'weather' or 'airquality': ")
        self.s.send(pickle.dumps(self.command))

    def recv_data(self):
        # Господине, pickle.dump()-нали сте информацията, която се връща 2 пъти
        self.data = pickle.loads(pickle.loads(self.s.recv(1024)))

    def est_connection(self):
        self.s.connect((self.ip, self.port))
        self.send_data()
        self.recv_data()
        self.s.close()

    def print_data(self):
        if self.command != "weather":
            print(self.data)
            save_data(self.data, self.command)
        else:
            print(self.data[0]["main"])
            save_data(self.data[0]["main"], self.command)

def data_exchange(client1):
    if not isinstance(client1, Client):
        raise ValueError("Object not compatible")

    while True:
        if client1.s.fileno() == -1:
            client1.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client1.est_connection()
        client1.print_data()

        if input("Type 1 to reestablish the connection: ") != '1':
            break


client = Client(IP, PORT)
data_exchange(client)
