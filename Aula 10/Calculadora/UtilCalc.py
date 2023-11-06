'''
    Criando funcs da caulculadora
'''

from functools import *

class Calculadora:

    # Func de soma da calculadora
    def somar(self, *args):
        return sum(args)

    # Func de subtracao da calculadora
    def subtrair(self, *args):
        return reduce(lambda x, y: x - y, args)

    # Func de multiplicacao da calculadora
    def multiplicar(self, *args):
        return reduce(lambda x, y: x * y, args)

    def dividir(self, *args):
        return reduce(lambda x, y: x / y, args)

'''

|====================================================|

'''

calc = Calculadora()

print (calc.somar(10, 5, 5))
print (calc.subtrair(10, 5, 5))
print (calc.multiplicar(10, 5, 5))
print (calc.dividir(10, 5, 5))