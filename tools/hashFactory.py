import hashlib
from termcolor import colored

def stringToHash():
  hashvalue = input(colored("Enter a string to hash: ",'blue'))

  hashobj1 = hashlib.md5()
  hashobj1.update(hashvalue.encode())
  print(colored("MD5 hash: " + hashobj1.hexdigest(),'yellow'))

  hashobj2 = hashlib.sha1()
  hashobj2.update(hashvalue.encode())
  print(colored("SHA1 hash: " + hashobj2.hexdigest(),'blue'))

  hashobj3 = hashlib.sha224()
  hashobj3.update(hashvalue.encode())
  print(colored("SHA224 hash: " + hashobj3.hexdigest(),'yellow'))

  hashobj4 = hashlib.sha256()
  hashobj4.update(hashvalue.encode())
  print(colored("SHA256 hash: " + hashobj4.hexdigest(),'blue'))

  hashobj5 = hashlib.sha512()
  hashobj5.update(hashvalue.encode())
  print(colored("SHA512 hash: " + hashobj5.hexdigest(),'yellow'))



def tryopen(wordlist):
	global passfile
	try:
		passfile = open(wordlist, "r")
	except FileNotFoundError:
		print(colored("[!!] No such file at that path. :( ", "red"))
		quit()

def md5ToString():
	md5hash = input(colored("[?] Enter md5 Hash value: ",'yellow'))
	wordlist = input(colored("[?] Enter path to wordlist: ",'yellow'))
	tryopen(wordlist)
	
	for password in passfile:
		print(colored("[-] trying: " + password.strip("\n"), "red"))
		enc_word = password.encode("utf-8")
		md5digest = hashlib.md5(enc_word.strip()).hexdigest()
	
		if md5digest == md5hash:
			print(colored("[+] The password is: " + str(password) ,"green"))
			exit(0)
	
	print(colored("Password not in passwordlist. :(","yellow"))



def sha1ToString():
	sha1hash = input(colored("[?] Enter sha1 Hash value : ",'yellow'))
	passlist = input(colored("[?] Enter Wordlist path : ",'yellow'))
	passfile = open(passlist,'r').readlines()

	for password in passfile:
		hashguess = hashlib.sha1(password.strip('\n').encode()).hexdigest()
		if hashguess == sha1hash:
			print(colored("[*] The password is: " + str(password) ,"green"))
			quit()
		else:
			print(colored("[*] Password guess " + str(password) + " doesn't match :( ", "red"))

	print(colored("Password not in passwordlist. :(","yellow"))

def main():
  tools = ['String -> Hash','MD5 -> String','SHA1 -> String']
  print(colored("\n Index       Action \n",'blue'))
  for tool in tools:
    print(colored("[  " + str(tools.index(tool)+1)+"  ]      "+ tool,'blue'))
  print(colored('[  0  ]      Exit','red'))  
  selected = input(colored('\n[?] HashFactory@choose~option : ','yellow'))
  if selected == '1':
    stringToHash()
  elif selected == '2':
    md5ToString()
  elif selected == '3':
    sha1ToString()
  else:
    print(colored(' [!!] Exiting...','red')) 
