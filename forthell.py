#FORTHELL

import socket
from threading import Thread
import os
from Crypto.Cipher import AES
import copy#custom module
import sys


argument = sys.argv
if "--help" in argument:
    print("ini help")
    sys.exit()
if "-p" or "--p" in argument:
    try:
        pbrp = argument.index("-p")
    except:
        try:
            prbp = argument.index("--p")
            
        except:
            print("error while getting port from user")

#pake settingan dari argument/file configuration(bisa ubah html)
#bind multiple port
#kalo ctrl+c minta settingan lagi
#bind semua protokol (ping, udp)
#prevent ddos
#package filter
#close port
#belajar kriptografi,tkj
print("starting firewall...")
spab = lambda x: [print(" ") for i in range(x)]
def decor(x):
    spab(1)
    symb = "*"
    [print(symb * len(x))]
    print(x)
    [print(symb * len(x))]
    spab(1)

def logg(pesan):
    filename = "firewall2.log"
    if (not os.access(filename, os.W_OK)):
        open(filename, "w+")
    else:
        print("[WARNING] log file exist")
    with open(filename, "a+") as logg:
        logg.write(pesan)

class crypto:
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.key = "kevinagusto12345"
        self.iv = "kevinagusto12345"
        self.aes = AES.new(self.key, self.mode, self.iv)
    def encrypt(self, data):
        try:
            data = data.encode("utf-8")
        except:
            pass
        
        
class iofile:
    def readfile(file):
        with open(file, mode="rb") as readfile:
            return readfile.read()
    def writefile(src, dst):
        if (os.access(dst, os.W_OK)):
            print("[WARNING] file already exist. try to rewrite")
        else:
            open(dst, "w+")
        with open(dst, "wb") as tulis:
            tulis.write(src)
        
            

#trying to looking self ip
ip = os.popen("ifconfig").read().split()
try:
    int(ip[101][0])
    ip = str(ip[101])
    print("self ip: %s" %(ip))
except:
    ip = input("self ip: ")
    if ip == "":
        ip = ""

granted_ip = ["192.168.43.171", "192.168.100.3.", "192.168.43.1"]
granted_port = {80, 443, 21, 22, 23}


port = [80, 443, 21, 22, 23, 8080, 5900, 5901]
protocol = ["socket.socket(socket.AF_INET, socket.SOCK_STREAM)", "socket.socket(socket.AF_INET, socket.SOCK_DGRAM)", "socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP"]


#lets all protocols with all ports
for i in protocol:
    for a in port:
        try:
            to_bind = "%s.bind((%s, %d))" %(i, ip, a)
            to_listen = "%s.listen()" %(i)
            exec(to_bind)
            exec(to_listen)
        except:
            continue
            

allfiles = [
 "login-firewall.html",
 "login-firewall.css",
 "denied.html",
 "denied.css",
 "granted.html",
 "granted.css"]

    
def filereader(x):
    reader = []
    for i in allfiles:
        with open(i, "rb") as tempr:
            oke = tempr.read()
            reader.append(oke)
    return reader[int(x)]
        

class firewall2:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen()
            
    def filtering(self, data, info):
        #info berbentuk [ip_src, port_src]
        #data ya data...ntar
        if (info[0] not in granted_ip):
            return False
        
    def handler(self, client_socket, info):
        terima_data = client_socket.recv(1024)
        print(terima_data)
        terima_data = terima_data.decode("utf-8").split()
        #just trying to send additional data
        for i in allfiles:
            for a in terima_data:
                if i in a:
                    with open(i, "rb") as to_send:
                        to_send = to_send.read()
                        client_socket.send(to_send)
                        client_socket.close()
                        return
                    
        gord = self.filtering(terima_data, info)
        if not gord:
            #trying to send login page
            with open(allfiles[0], "rb") as loginn:
                loginn = loginn.read()
                client_socket.send(loginn)
            return
        #kalau ga ada masalah ya sudah
        decor(print("access granted on" %(info)))
        
        
    def run(self):
        decor("guarding port: 80")
        while True:
            client, addr = self.server.accept()
            spab(1)
            decor("connection from %s:%d" %(addr[0], addr[1]))
            spab(1)
            Thread(target=self.handler, args=[client, addr]).start()
            
if "__name__" == __main__:        
 firewall2().run()        