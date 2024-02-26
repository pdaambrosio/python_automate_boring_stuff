#!/home/pdajgs/python_labs/py3.7/bin/python3

# Acrescenta marcadores da Wikipedia no inicio de cada texto

import pyperclip
text = pyperclip.paste()

# Separa as linhas e acrescenta o texto
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)