def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 <= 0:
        return 'Impossível dividir por zero ou número negativo'
    else:
        return num1 / num2