#1 - import bibliotecas
import pytest

#2 class - classe

#3 definitions metods e funções
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def somar(numero1, numero2):
    return numero1 + numero2
def subtrair(numero1, numero2):
    return numero1 + numero2
def multiplicar(numero1, numero2):
    return numero1 + numero2
def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
def test_somar():
    assert somar(2,2) == 4
def test_subtrair():
    assert somar(4,5) == -1
def test_multiplicar():
    assert somar(3,7) == 21
def test_dividir():
    assert dividir(8,4) == 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
