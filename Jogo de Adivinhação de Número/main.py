import random

def jogar_adivinhacao():
    # Selecionar a dificuldade
    print("Bem-vindo ao jogo de adivinhação!")
    print("Escolha a dificuldade:")
    print("1 - Fácil (números de 1 a 10)")
    print("2 - Médio (números de 1 a 100)")
    print("3 - Difícil (números de 1 a 1000)")
    
    dificuldade = int(input("Digite o número da dificuldade escolhida: "))
    if dificuldade == 1:
        limite_superior = 10
        max_tentativas = 5
    elif dificuldade == 2:
        limite_superior = 100
        max_tentativas = 10
    else:
        limite_superior = 1000
        max_tentativas = 15
    
    # Configurações iniciais
    numero_sorteado = random.randint(1, limite_superior)
    tentativas = 0
    pontos = 100
    historico_tentativas = []

    # Função para fornecer dicas opcionais
    def fornecer_dica(numero):
        if numero % 2 == 0:
            print("Dica: O número é par.")
        else:
            print("Dica: O número é ímpar.")
        if numero % 5 == 0:
            print("Dica: O número é múltiplo de 5.")

    # Loop principal do jogo
    while tentativas < max_tentativas:
        print(f"\nTentativa {tentativas + 1} de {max_tentativas}.")
        chute = int(input(f"Digite um número entre 1 e {limite_superior}: "))
        
        # Verificar se o número já foi tentado
        if chute in historico_tentativas:
            print("Você já tentou esse número! Tente outro.")
            continue

        tentativas += 1
        historico_tentativas.append(chute)
        
        # Verificar o palpite
        if chute == numero_sorteado:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas!")
            pontos += 10 * (max_tentativas - tentativas)
            break
        elif chute < numero_sorteado:
            print("O número é maior.")
        else:
            print("O número é menor.")
        
        # Exibir dicas
        if tentativas % 3 == 0:  # Dica a cada 3 tentativas
            fornecer_dica(numero_sorteado)
        
        # Reduzir pontos por tentativa
        pontos -= 5

        # Exibir histórico de tentativas
        print("Histórico de tentativas:", historico_tentativas)
        
    # Fim do jogo
    if chute != numero_sorteado:
        print(f"\nQue pena! Você atingiu o número máximo de tentativas.")
        print(f"O número correto era {numero_sorteado}.")
    print(f"Sua pontuação final é: {pontos} pontos.")

# Iniciar o jogo
jogar_adivinhacao()
