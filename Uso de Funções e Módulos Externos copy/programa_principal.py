# Importa as funções da biblioteca 'minha_biblioteca'
from minha_biblioteca import exibirResultados

# Função principal que controla o fluxo do programa
def main():
    try:
        # O usuário fornece quantos números deseja consultar
        quantidade = int(input('Quantos números deseja consultar? (Digite -1 para sair): '))
        
        if quantidade == -1:
            print('Obrigado por utilizar o sistema!')
            return

        for i in range(quantidade):
            numero = int(input(f'Informe o número {i+1}: (Digite -1 para sair): '))
            
            if numero == -1:
                break  # Sai do loop e termina o programa imediatamente
            
            exibirResultados(numero)
            print()  # Adiciona uma linha em branco após cada consulta

    except ValueError:
        print('Entrada inválida, por favor, insira um número válido.')
    
    # A mensagem de agradecimento aparece uma única vez ao final
    print('Obrigado por utilizar o sistema!')

# Executa o programa
if __name__ == "__main__":
    main()
