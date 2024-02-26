#!/home/pdajgs/python_labs/py3.7/bin/python3

import pyautogui, time

# defina as variáveis com as coordenadas corretas obtidas em seu computador
nameField = (648,319)
submitButton = (651,817)
submitButtonColor = (75,141,249)
submitAnotherLink = (760,224)

formData = [{'name':'Alice','fear':'eavesdroppers','source':'wand','robocop':4,'comments':'Tell Bob I said hi.'},{'name':'Bob','fear':'bees','source':'amulet','robocop':4,'comments':'n/a'},{'name':'Carol','fear':'puppets','source':'crystal ball','robocop':1,'comments':'Please take the puppets out of the break room.'},{'name':'Alex Murphy','fear':'ED-209','source':'money','robocop':5,'comments':'Protect the innocent. Serve the public trust. Uphold the law.'}]

# definindo uma pausa para cada chamada da função
pyautogui.PAUSE = 0.5

for person in formData:
    # uma chance para encerrar o programa
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL+C <<<')
    time.sleep(5)
    # espera até a pagina do formulário tenha sido carregada
    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
        time.sleep(0.5)
    print('Entering %s info...' %(person['name']))
    pyautogui.click(nameField[0],nameField[1])
    # preenche o campo Name
    pyautogui.typewrite(person['name'] + '\t')
    # preenche o campo Greatest Fear(s)
    pyautogui.typewrite(person['fear'] + '\t')
    # preenche o campo Source of Wizard Powers
    if person['source'] == 'wand':
        pyautogui.typewrite(['down','\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down','down','\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down','down','down','down','\t'])
    # preenche o campo robocop
    if person['robocop'] == 1:
        pyautogui.typewrite(['','\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right','\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right','right','\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right','right','right','\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right','right','right','right','\t'])
    # preenche o campo adicional comments
    pyautogui.typewrite(person['comments'] + '\t')
    # clica em submit
    pyautogui.press('enter')
    # espera até que a pagina do formulário tenha sido carregada
    print('Clicked Submit.')
    time.sleep(5)
    # clica no link Submit another response
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])