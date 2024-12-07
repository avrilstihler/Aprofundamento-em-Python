# Solicita ao usuário quantos números deseja consultar
quantidade = int(input('Quantos números você deseja consultar? '))

# Inicializa a variável para a soma total
soma_total = 0

# Repete a solicitação de números conforme a quantidade fornecida
for i in range(quantidade):
    # Solicita o número do usuário
    numero = float(input('Digite um número para saber a soma com seus antecessores: '))
    
    # Calcula a soma dos antecessores e o próprio número
    soma = sum(range(1, int(numero) + 1))
    
    # Exibe o resultado da soma para o número atual
    print(f'A soma de {numero} com seus antecessores é: {soma}')
    
    # Adiciona ao total geral
    soma_total += soma

# Exibe a soma total ao final de todas as consultas
print(f'A soma total de todos os números consultados é: {soma_total}')

# Mensagem de agradecimento
print('Obrigado por usar o programa!')
