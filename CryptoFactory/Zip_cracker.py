import zipfile
from threading import Thread
import time

def extract_zip(zFile,passwd):
  duration = time.time() - curr_time
  
  try:
    zFile.extractall(pwd=bytes(passwd,'utf-8'))
    print("[+] Match Found : "+ passwd)
    print("[!] Exited at",duration,"Seconds")
  except: 
    pass

def main():
  #dictionary attack
  global curr_time
  curr_time = time.time()
  
  zname = input('Path of Encrypted Zip File : ')
  dname = input('Path of Dictionary file : ')
  
  zFile = zipfile.ZipFile(zname)
  passFile = open(dname , "r")
  print('[+] Cracking zip using Dictionary Attack')
  
  for line in passFile.readlines():
    passwd = line.strip("\n")
    t = Thread(target=extract_zip, args=(zFile,passwd))
    t.start()