# Função que calcula o fatorial de um número
def calcularFatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Função que calcula a soma dos pares ou ímpares de um número
def calcularSomatorio(numero, pares):
    resultado = 0
    inicio = 0 if pares else 1  # Se pares=True, começa do 0, senão, começa do 1
    for i in range(inicio, numero + 1, 2):
        resultado += i
    return resultado

# Função que exibe os resultados para o número fornecido
def exibirResultados(numero):
    print(f'O fatorial de {numero} é: {calcularFatorial(numero)}')
    print(f'A soma dos pares até {numero} é: {calcularSomatorio(numero, True)}')
    print(f'A soma dos ímpares até {numero} é: {calcularSomatorio(numero, False)}')
