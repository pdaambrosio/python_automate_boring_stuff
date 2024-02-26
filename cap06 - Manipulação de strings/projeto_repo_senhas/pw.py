#!/home/pdajgs/python_labs/py3.7/bin/python3

# pw.py = Repositorios de senhas não seguras

passwords = {'teste@gmail.com':'12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # o primeiro argumento da linha de comando é o nome conta

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)