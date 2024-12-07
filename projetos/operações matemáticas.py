# Solicita ao usuário para inserir dois números
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

# Solicita ao usuário para escolher uma operação
operacao = input('Escolha uma operação (+, -, *, /): ')

# Realiza a operação escolhida
if operacao == '+' or operacao == 'soma' :
    resultado = num1 + num2
    print('O resultado da soma dos números é:', resultado)
elif operacao == '-' or operacao == 'subtração' :
    resultado = num1 - num2
    print('O resultado da subtração dos números é:', resultado)
elif operacao == '*' or operacao == 'multiplicação' :
    resultado = num1 * num2
    print('O resultado da multiplicação dos números é:', resultado)
elif operacao == '/' or operacao == 'divisão' :
    if num2 != 0:
        resultado = num1 / num2
        print('O resultado da divisão dos números é:', resultado)
    else:
        print('Erro: Não é possível dividir por zero.')
else:
    print('Erro: Operação inválida.')
