#!/home/pdajgs/python_labs/py3.7/bin/python3

# calculando o tempo do codigo

import time

def calcProd():
    # calcula o produto dos 100.000 primeiros números
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd
endTime = time.time()

print('The result is %s digits long.' %len(str(prod)))
print('Took %s seconds to calculate.' %(endTime - startTime))