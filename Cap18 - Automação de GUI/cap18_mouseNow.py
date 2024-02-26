#!/home/pdajgs/python_labs/py3.7/bin/python3

# passo1 - importar o modulo
import pyautogui

# passo2 - codigo de saída para o loop infinito
print('Press CTRL+C to quit')

try:
    while True:
# passo3 - obter e exibir as coordenadas no mouse 
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
