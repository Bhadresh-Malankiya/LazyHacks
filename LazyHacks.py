from time import sleep, time
from tools import MITM,portScanner,ARPscan,Zip_cracker,Crypto,BackdoorServer,sshBrute,hashFactory
from termcolor import colored

def loading(t):
  input(colored('\n [+] Press Enter to continue ...','green'))
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
    'sshBrute - Linux Only',
    'HashFactory',
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
    num = input(colored('\n LazyHacks@chooseOption~#$ ','green'))
    print('\n')
    if num == '0' or num == '00':
      print('\n [!!] Exiting...')
      exit(0)
    elif num == '1' or num == '01':
      tools.MITM.main()
      loading(3)
      main()
    elif num=='2' or num == '02':
      portScanner.main()
      loading(3)
      main()
    elif num=='3' or num == '03':
      ARPscan.main()
      loading(3)
      main()
    elif num=='4' or num == '04':
      Zip_cracker.main()
      loading(3)
      main()
    elif num=='5' or num == '05':
      Crypto.main()
      loading(5)
      main()
    elif num=='6' or num == '06':
      BackdoorServer.main()
      loading(5)
      main()
    elif num=='7' or num == '07':
      sshBrute.main()
      loading(5)
      main()
    elif num=='8' or num == '08':
      hashFactory.main()
      loading(5)
      main() 
    else:
      print(colored('\n [!!] Total 8 options are Working Choose Between 0-8 ','red'))
      loading(5)
      main()
  except KeyboardInterrupt:
    print(colored('\n [!!] Exiting Keyboard Intrrupted.','red'))

if __name__ == '__main__':
  main()
  