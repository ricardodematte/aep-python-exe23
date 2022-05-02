'''
A Loja Mamão com Açúcar está vendendo seus produtos em 12 (doze)
prestações sem juros. Faça um algoritmo que receba um valor de uma
compra e mostre o valor das prestações em 12 vezes.
'''

import os
valor = (float(input("Digite o valor do produto:\n")))
prest = valor/12
os.system("clear")
print ("A prestação é R$",prest)