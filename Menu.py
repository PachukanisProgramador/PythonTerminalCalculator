import this
import Operacoes

this.opcao = 0
this.num1 = 0
this.num2 = 0


def menu():
    this.opcao = int(
        input('Determine a operação que deseja realizar\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n'))


def coletarNum1():
    this.num1 = float(input('Insira o primeiro número: '))


def coletarNum2():
    this.num2 = float(input('Insira o segundo número: '))


def loop():
    i = 0
    while i < 4:
        print(i)
        i += 1


def executar():
    this.looping = True

    while this.looping:
        menu()

        if this.opcao == 0:
            this.looping = False
            print('Obrigado por usar o meu primeiro programa em Python!')

        elif this.opcao == 1:
            coletarNum1()
            coletarNum2()
            print('{} + {} = {}'.format(this.num1, this.num2, Operacoes.soma(this.num1, this.num2)))

        elif this.opcao == 2:
            coletarNum1()
            coletarNum2()
            print('{} - {} = {}'.format(this.num1, this.num2, Operacoes.subtracao(this.num1, this.num2)))

        elif this.opcao == 3:
            coletarNum1()
            coletarNum2()
            print('{} X {} = {}'.format(this.num1, this.num2, Operacoes.multiplicacao(this.num1, this.num2)))

        elif this.opcao == 4:
            coletarNum1()
            coletarNum2()
            if this.num2 <= 0:
                print(Operacoes.divisao(this.num1, this.num2))
            else:
                print('{} / {} = {}'.format(this.num1, this.num2, Operacoes.divisao(this.num1, this.num2)))

        else:
            print('Digite um valor válido!')
