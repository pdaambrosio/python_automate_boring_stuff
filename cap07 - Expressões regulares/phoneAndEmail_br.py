#!/home/pdajgs/python_labs/py3.7/bin/python3

import pyperclip,re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # codigo de aréa
    (\s|-|\.)?                        # separador
    (\d{1})?                          # digito 9 para celulares
    (\s|-)?                           # separador
    (\d{4})                           # primeiros 4 digitos
    (\s|-|\.)                         # separador
    (\d{4})                           # últimos 4 digitos
    # (\s*(ext|x|ext.)\s*(d{2,5}))?     # extensão
)''',re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                  # nome do usuário
    @                                  # arroba
    [a-zA-Z0-9.-]+                     # nome do domínio
    (\.[a-zA-Z{2,4}])?                 # ponto seguido de outros caracteres
)''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += 'x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')