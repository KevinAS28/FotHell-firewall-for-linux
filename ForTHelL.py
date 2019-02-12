#!/usr/bin/python3

#next time...
#usahakan jaringan terenkripsi
#firewall (tcp, udp, icmp) multiple port
#attack ddos
#ftp
#send signal biasa
#pake settingan dari argument/file configuration(bisa ubah html)
#bind multiple port
#kalo ctrl+c minta settingan lagi
#bind semua protokol (ping, udp)
#prevent ddos
#package filter
#close port
#belajar kriptografi,tkj
#hanya yang login bisa ubah settingan. kalo udah ubah setting, restart firewall dengan settingan baru
#bukan hanya ubah settingan, bisa melakukan fungsi lainnya
#nanti settingannya di dalam file dan di enkrip
#fitur black hat?

import socket
from threading import Thread
import os
import sys
import subprocess
import re
import getpass
import time
import zipfile
import urllib
###custom module###
import urlcrypt
from C_AES import AES_Crypto
from get_values_html import get_values
from get_values_html import get_file
configuration_file = "FortHell.conf"
youtryit = []
blocked_ip = []
granted_ip = ["127.0.0.1", "localhost"]
#sojb = ["socket.socket(socket.AF_INET, socket.SOCK_STREAM)", "socket.socket(socket.AF_INET, socket.SOCK_DGRAM)", "socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP"]
#list_file = ["loginnet.html", "loginnet.css", "login-firewall.html", "login-firewall.css", "denied.html", "denied.css", "main.html", "main.css", "ForTHelL.log", "log_file.html", "black-hole.jpg", "hell1.jpg", "log_file.css"]
#valid_username = ["kevin", "xyregz"]
#valid_password = ["otsuganivek", "xyz"]
#file_log = "ForTHelL.log"
#aespassword = "passwordpassword"#//
#aesiv = "drowssapdrowssap"#//
print("Starting FortHell...")
def confreader(x, mode="r"):
    if mode=="r":
        with open(configuration_file, "r+") as conf:
            conf = conf.read().split("\n")
            return conf[x]
def confwriter(x, y):       
    with open(configuration_file, "r+") as cf:
        cf = cf.read()
        cf = cf.replace(x, y)
        with open(configuration_file, "w+") as cw:
            cw.write(cf)
        return True	
        


spab = lambda x: [print(" ") for i in range(x)]

def logg(text, thefile="log"):
    if thefile=="log":
        with open(file_log, "a+") as log:
            log.write(str(time.ctime()))
            log.write(" ")
            log.write(text)
            log.write("\n")
    if thefile=="ip_permissions":
        with open(thefile, "a+") as oke:
            oke.write("%s\n%s\n\n" %(str(time.ctime()), text) )
    if thefile=="log_get":
        with open(thefile, "a+") as eko:
            eko.write("%s\n%s\n\n\n" %(str(time.ctime()), text) )


def file_reader(x, ex=""):
    
    with open(list_file[x] if not len(ex) else list_file[x] + ex, "rb") as oke:
        eko = oke.read()
        return eko
def decor(text, symb="#"):
    print(symb*len(str(text)))
    print(text)
    print(symb*len(str(text)))
def block_ip(x):
    try:
        order = "iptables -A INPUT -s %s -j DROP" %(x)
        logg("Ip blocked: %s" %(str(x)))
        subprocess.check_output(order, shell=True)
        logg("ip blocked: %s" %(x), "ip_permissions")
        #blocked_ip.append(x)
        decor("IP blocked: %s" %(x))
        
        return True
    except:
        logg("Unable to block ip %s" %(x))
        return False

def unblock_ip(x):
    try:
        order = "iptables -D INPUT -s %s -j DROP" %(x)
        logg("Ip unblocked: %s" %(str(x)))
        subprocess.check_output(order, shell=True)
        logg("ip unblocked: %s" %(x), "ip_permissions")
        #blocked_ip.remove(x)
        decor("unblocking ip: %s" %(x))
        return True
    except:
        logg("cannot unblock ip %s" %(x))
        return False

def compress(*file_namee, enc=False):
    for file_name in file_namee:
        with zipfile.ZipFile(file_namee[0] + ".zip", "w") as eko:
            eko.write(file_name)    

                
def oflogin():
    username = str(input("Login to ForTHelL.Net: "))
    password = str(getpass.getpass("Password: "))
    try:
        valid_username.index(username)
        valid_password.index(password)
        if valid_password[valid_username.index(username)] != password:
            raise TypeError
        if valid_username[valid_password.index(password)] != username:
            raise TypeError
    except:
        print("Login Fail")
def cleanth():
    time.sleep(1)
    youtryit.clear()
    
class onlogin():
    
    def __init__(self):
        time.sleep(3)
        
        #we need to create simple tcp server
        __ip = ""   
        __port = 80
        to_run = "self.tcp = %s" %(sojb[0])
        exec(to_run)
        try:
            self.tcp.bind((__ip, __port))
        except:
            print("The Firewall system need delay to restart\nplease exit and wait a momment")
            sys.exit(0)
        self.tcp.listen()
        logg("Login via online is now availble")
        print("Login via online is now availble")
        
    def __client_handler(self, client_socket, info):
        try:
            terimapure = client_socket.recv(1024)
            try:
             terima = terimapure.decode("utf-8")
            except:
                open("research", "w+")
                with open("research", "wb") as tuliss:
                    tuliss.write(terimapure)
                terima = terimapure[0:100].decode("utf-8")
                decor(terima)
            try:
             logg(terima, thefile="log_get")
            except:
                logg("FILE from", thefile="log_get")
            #anticipation for DDOS Attack
            #print(terimapure)#################
            youtryit.append(info[0])
            if (youtryit.count(info[0])) > 25:
                block_ip(info[0])
                logg("[WARNING] %s:%d try to DDOS ATTACK" %(info[0], info[1]))
            if len(terima) > 999999999999999999999999999:
                block_ip(info[0])
                client_socket.close()
                logg("[WARNING] %s:%d try to DDOS ATTACK" %(info[0], info[1]))
            try:
             terima1 = terima.split()
            except:
                #file
                terima1 = terima[0:4]
                decor(terima1)
            def normal_sender(*to_send):
                #client_socket.sendall(b"""HTTP/1.1 200 OK\nContent-Type: text/html""")
                
                #client_socket.close()
                
                for i in to_send:
                    ###print(i)
                    client_socket.send(i)
                client_socket.close()
                
            
            
            if not info[0] in granted_ip:
                for i in terima1:
                    if "hell1.jpg" in i:
                        normal_sender(file_reader(11))
                        return        
                    if "loginnet.css" in i:
                        normal_sender(file_reader(1))
                        return
                    if "Username" in i:
                        unps = i.replace("&", "=")
                        unps = unps.split("=")
                        users = unps[1]
                        passs = unps[3]
                        #users = get_values("Username", terima)
                        #passs = get_values("password", terima)
                        logg("%s:%d %s %s is try to login via online" %(info[0], info[1], users, passs))
                        print("%s:%d %s %s is try to login via online" %(info[0], info[1], users, passs))
                        
                        #are you intruder, or user?
                        ioru = False
                        try:
                            yoyo = valid_username.index(users)
                            if valid_password[yoyo] != passs:
                                raise TypeError
                            ioru = True
                        except:
                            pass
                        if ioru:
                            normal_sender(file_reader(17))
                            granted_ip.append(info[0])
                            return
                        else:
                            client_socket.send(file_reader(4))
                            block_ip(info[0])
                            return
                        client_socket.close()
                        return
                    
                    
                logg("%s:%d is access online login page" %(info[0], info[1]))
                print("%s:%d is access online login page" %(info[0], info[1]))                
                client_socket.send(file_reader(0))
                client_socket.close()
                
                return
            try:
                if terima1[0] == "GET" or (b"GET" in terimapure[0:10]):
                    for i in terima1:
                    #if "POST" in i:
                        if "progress.css" in i:
                            normal_sender(file_reader(18))
                            return
                        if "log_poget.txt" in i:
                            normal_sender(file_reader(15))
                            return
                        if "ip_permissions" in i:
                            normal_sender(file_reader(14))
                            return                    
                        if "hell1.jpg" in i:
                            normal_sender(file_reader(11))
                            return                
                        if configuration_file in i:
                            normal_sender(file_reader(13))
                            return
                        if "home.html" in i:
                            normal_sender(file_reader(6))
                            return
                        if "FortHell.txt" in i:
                            normal_sender(file_reader(8))
                            return
                        if "main.css" in i:
                            normal_sender(file_reader(7))
                            client_socket.close()
                            return                    
                        if "log_file.css" in i:
                            normal_sender(file_reader(12))
                            return
                        if "black-hole.jpg" in i:
                            normal_sender(file_reader(10))
                            return
                        if "log_file.html" in i:
                            logg("%s:%d accessing log file via online" %(info[0], info[1]))
                            normal_sender(file_reader(9))
                            return
                        if "denied.css" in i:
                            client_socket.send(file_reader(5))
                            client_socket.close()
                            return
                        if "run_command.html" in i:
                            normal_sender(file_reader(16))
                            logg("%s:%d accessing command page"%(info[0], info[1]))
                            return
                        if "Enc_Dec.html" in i:
                            normal_sender(file_reader(19))
                            logg("%s:%d accessing crypto page" %(info[0], info[1]))
                            return
            except:
                yaudah = 0
            try:        
                if (terima1[0] == "POST") or (b"POST" in terimapure[0:10]):
                    decor("dapat post")
                    if b"POST" in terimapure[0:10]:
                        decor("ADA FILE")
                    for i in terima1:
                        try:
                            if "in-command" in i:
                                print("INI IN COMMAND")
                                i = terima
                                #in_command = urlcrypt.decrypt(get_values("in-command", i))
                                #in_command = in_command.replace("+", " ")
                                #decor("COMMAND: %s" %(urlcrypt.urldec(i[-1])))
                                in_command = re.sub("\+", " ", urlcrypt.decrypt(get_values("in-command", i)))
                                decor("IN-COMMAND: %s" %(in_command))
                                logg("IN-COMMAND: %s" %(in_command))
                                try:
                                    eval(in_command)
                                except:
                                    try:
                                        eval(in_command)
                                    except:
                                        logg("Failed to run command %s" %(in_command))
                                normal_sender(file_reader(16))
                                return
                                
                            if "ex-command" in i:
                                print("INI EX COMMAND")
                                i = terima
                                #ex_command = urlcrypt.decrypt(get_values("ex-command", i))
                                #ex_command = ex_command.replace("+", " ")
                                ex_command = re.sub("\+", " ", urlcrypt.decrypt(get_values("ex-command", i)))
                                decor("EX-COMMAND: %s" %(ex_command))
                                logg("EX-COMMAND: %s" %(ex_command))
                                try:
                                    subprocess.check_output(ex_command, shell=True)
                                except:
                                    try:
                                        subprocess.check_output(ex_command, shell=True)
                                    except:
                                        logg("Failed to run command %s" %(ex_command))
                                normal_sender(file_reader(16))
                                return
                                
                            if "melarang" in i:
                                #i = terima.split("=")
                                #i = i[-2].split("&")[0]
                                i = re.sub("\+", " ", urlcrypt.decrypt(get_values("melarang-ip", terima)))
                                block_ip(i)
                                
                            if "membolehkan" in i:
                                #i = terima.split("=")
                                #i = i[-2].split("&")[0]
                                i = re.sub("\+", " ", urlcrypt.decrypt(get_values("membolehkan-ip", terima)))
                                unblock_ip(i)
                            if "AES_DATA" in i:
                                #decor("REQUEST AES")
                                i = terima
                                aesdata = urlcrypt.decrypt(re.sub("\+", " ", get_values("AES_DATA", i)))
                                #print(aesdata)
                                aespswd = urlcrypt.decrypt(re.sub("\+", " ", get_values("AES_PASSWORD", i)))
                                #print(aespswd)
                                aesiv = urlcrypt.decrypt(re.sub("\+", " ", get_values("AES_IV", i)))
                                #print(aesiv)
                                aesmode = get_values("AES_MODE", i)
                                #print(aesmode)
                                enc_dec = get_values("AES_CRYPTO", i)
                                #print(enc_dec)
                                return
                        except:
                            pass
                        if b"Content-Type: multipart/form-data" in terimapure:
                            berkass = get_file(terima)
                            open("my_file", "w+")
                            with open("my_file", "wb") as yoktul:
                                yoktul.write(berkass)
                            decor("mungkin file?", symb="+")
            except:
                yaudah = 0
                    
            
            #client_socket.send(file_reader(6))
            normal_sender(file_reader(6))
            logg("%s:%d is accessing firewall system" %(info[0], info[1]))
            #granted_ip.append(info[0])                                
            #client_socket.close()
            return
        except KeyboardInterrupt:
            try:
                client_socket.close()
                try:
                    self.tcp.close()
                except:
                    pass
                try:
                    self.tcp.shutdown()
                except:
                    pass
                try:
                    self.tcp.shutdown(socket.SHUT_RD)
                except:
                    pass
            except:
                logg("ERROR while close connection during stop online login")
                return
            return
        return
    def run(self):
        while True:
            try:
                client, addr = self.tcp.accept()

                Thread(target=self.__client_handler, args=[client, addr]).start()
                Thread(target=cleanth).start()
            except KeyboardInterrupt:
                try:
                    self.tcp.close()
                except:
                    pass
                try:
                    client.close()
                except:
                    pass
def renewlog():               
    #renew the log file
    time.sleep(3)
    if os.access("ip_permissions", os.W_OK):
        os.remove("ip_permissions")
    open("ip_permissions", "w+")
    with open("ip_permissions", "a+") as oke:
        oke.write("%s\nn" %(str(time.ctime())))    
    if os.access(file_log, os.W_OK) or os.access("FortHell.txt", os.W_OK):
        os.remove(file_log)
        with open(file_log, "w+") as oke:
            oke.write("ForTHelL\nstart at %s\n" %(str(time.ctime())))
    if os.access(log_get, os.W_OK):
        os.remove(log_get)
    open(log_get, "w+")
    with open(log_get, "a+") as oke:
        oke.write("%s\nn" %(str(time.ctime()))) 
    if os.access("log_get", os.W_OK):
        os.remove("log_get")
    open("log_get", "w+")
def startonlogin():
    onlogin().run()
Thread(target=renewlog).start()            
Thread(target=startonlogin).start()

while True:
    exec(confreader(0)) #sojb
    exec(confreader(2)) #valid_username
    exec(confreader(3)) #valid_password
    exec(confreader(4)) #file_log
    exec(confreader(5)) #aespassword
    exec(confreader(6)) #aesiv
    exec(confreader(7)) #log_get
    exec(confreader(8)) #binary dictionary
    exec(confreader(1)) #list_file    
    time.sleep(3)
    


