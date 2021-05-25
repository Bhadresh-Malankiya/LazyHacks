from time import sleep, time
from tools import MITM,portScanner,ARPscan,Zip_cracker,Crypto,BackdoorServer,sshBrute
from termcolor import colored

def loading(t):
  animation = "|/-\\"
  idx = 0
  while (idx/5) < t:
    print(colored("   Loading .... [  " +animation[idx % len(animation)] + "  ]                                                       ",'yellow'), end = "\r")
    idx +=1
    sleep(0.2)

def main():
  banner = '''
           .------..------..------..------..------..------..------..------..------.
           |L.--. ||A.--. ||Z.--. ||Y.--. ||H.--. ||A.--. ||C.--. ||K.--. ||S.--. |
           | :/\: || (\/) || :(): || (\/) || :/\: || (\/) || :/\: || :/\: || :/\: |
           | (__) || :\/: || ()() || :\/: || (__) || :\/: || :\/: || :\/: || :\/: |
           | '--'L|| '--'A|| '--'Z|| '--'Y|| '--'H|| '--'A|| '--'C|| '--'K|| '--'S|
           `------'`------'`------'`------'`------'`------'`------'`------'`------'
  '''

  art = '''
  ----------------------------------------------------------------------------------------------
  '''
  toolList = [
    'Man In The Middle Automation',
    'Port Scanner',
    'ARP Scanner',
    'Zip File Cracker',
    'Crypto For Files',
    'Start Advance Backdoor Server',
    'sshBrute',
    'HashCracker',
    'DDoS Automations',
    'FtpBrute'
    ]
  print(colored(banner,'red') + '\n')
  print(colored(art,'yellow') + '\n')
  print(colored(' Index            Tool Name', 'blue')+'\n')
  for i in toolList:
    if toolList.index(i) < 9:
      index = '0' + str(toolList.index(i) + 1)
    else:
      index = str(toolList.index(i) + 1)
    print(colored('[  '+ index + '  ]         ' +i , 'blue'))
  print(colored('[  00  ]         '+'Exit' , 'red'))  
  try:
    num = input(colored('\n LazyHacks@choose~option~$ ','green'))
    print('\n')
    if num == '0':
      exit(0)
    elif num == '1':
      MITM.main()
      loading(5)
      main()
    elif num=='2':
      portScanner.main()
      loading(5)
      main()
    elif num=='3':
      ARPscan.main()
      loading(5)
      main()
    elif num=='4':
      Zip_cracker.main()
      loading(5)
      main()
    elif num=='5':
      Crypto.main()
      loading(5)
      main()
    elif num=='6':
      BackdoorServer.main()
      loading(5)
      main()
    elif num=='7' :
      sshBrute.main()
      loading(5)
      main()
    else:
      print(colored('\n [!!] Total 10 options are Added Choose Between 1 to 10','red'))
      loading(5)
      main()
  except KeyboardInterrupt:
    print(colored('\n [!!] Exiting Keyboard Intrrupted.','red'))

if __name__ == '__main__':
  main()
  