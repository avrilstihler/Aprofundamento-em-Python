class Aluno:
    def __init__(self, nome, notas, frequencia):
        self.nome = nome
        self.notas = notas
        self.frequencia = frequencia


class Monitoramento:
    def __init__(self, aluno):
        self.aluno = aluno

    def calcular_media(self):
        return sum(self.aluno.notas) / len(self.aluno.notas)

    def verificar_risco(self):
        media = self.calcular_media()
        return self.aluno.frequencia < 75 or media < 7.0


class Evasao:
    def __init__(self, monitoramento):
        self.monitoramento = monitoramento

    def verificar_evasao(self):
        return self.monitoramento.verificar_risco()


# Programa Principal
def main():
    alunos = []

    print("=== Sistema de Monitoramento de Evasão Escolar ===")
    
    while True:
        print("\nDigite os dados do aluno:")
        nome = input("Nome do aluno: ")
        frequencia = float(input("Frequência do aluno (%): "))
        notas = list(map(float, input("Notas do aluno (separe por espaços): ").split()))
        
        aluno = Aluno(nome, notas, frequencia)
        alunos.append(aluno)
        
        opcao = input("\nDeseja adicionar outro aluno? (s/n): ")
        if opcao.lower() != 's':
            break

    print("\n=== Resultados ===")
    for aluno in alunos:
        monitoramento = Monitoramento(aluno)
        evasao = Evasao(monitoramento)

        media = monitoramento.calcular_media()
        risco = evasao.verificar_evasao()

        print(f"\nAluno: {aluno.nome}")
        print(f"Frequência: {aluno.frequencia}%")
        print(f"Média das Notas: {media:.2f}")
        print(f"Risco de Evasão: {'Sim' if risco else 'Não'}")


if __name__ == "__main__":
    main()
