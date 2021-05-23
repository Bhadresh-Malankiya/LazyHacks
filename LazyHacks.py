from time import sleep, time
from tools import MITM,portScanner,ARPscan,Zip_cracker,Crypto,BackdoorServer
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
    'Start Advance Backdoor Server'
    ]
  print(colored(banner,'red') + '\n')
  print(colored(art,'yellow') + '\n')
  print(colored(' Index            Tool Name', 'blue')+'\n')
  for i in toolList:
    print(colored('[  '+str(toolList.index(i)+1) + '.  ]         ' +i , 'blue'))
  print(colored('[  0.  ]         '+'Exit' , 'red'))  
  try:
    num = input(colored('\n Choose Tool : ','green'))
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
    else:
      print(colored('\n [!!] Total 5 options are Added Choose Between 1 to 5','red'))
      loading(5)
      main()
  except KeyboardInterrupt:
    print(colored('\n [!!] Exiting Keyboard Intrrupted.','red'))

if __name__ == '__main__':
  main()
  