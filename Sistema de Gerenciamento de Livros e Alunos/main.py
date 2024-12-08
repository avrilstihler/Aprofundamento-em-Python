class Livro:
    def __init__(self, titulo, autor, codigo_identificacao):
        self._titulo = titulo
        self._autor = autor
        self._codigo_identificacao = codigo_identificacao
        
    def imprimir(self):
        print("Dados do livro:")
        print(f"Título: {self._titulo}, Autor: {self._autor}, Código de Identificação: {self._codigo_identificacao}")

    def set_titulo(self, titulo):
        self._titulo = titulo  # Permite alterar o título
        print(f"\nO novo título do livro é: {self._titulo}")  # Mensagem ao alterar

    def set_autor(self, autor):
        self._autor = autor  # Permite alterar o autor
        print(f"O novo autor do livro é: {self._autor}")  # Mensagem ao alterar

    def set_codigo_identificacao(self, codigo_identificacao):
        self._codigo_identificacao = codigo_identificacao  # Permite alterar o código de identificação
        print(f"O novo código de identificação do livro é: {self._codigo_identificacao}")  # Mensagem ao alterar
        
    def get_titulo(self):
        return self._titulo  # Retorna o título

    def get_autor(self):
        return self._autor  # Retorna o autor

    def get_codigo_identificacao(self):
        return self._codigo_identificacao  # Retorna o código de identificação

# Criando um objeto da classe Livro
livro = Livro("O Ceifador", "Neal Shusterman", "1204")
livro.imprimir()

# Alterando atributos usando os métodos set
livro.set_titulo("A Nuvem")
livro.set_autor("Neal Shusterman")
livro.set_codigo_identificacao("1205")

# Imprimindo novamente para ver as alterações
print("\nApós as alterações:")
livro.imprimir()


class Aluno:
    def __init__(self, nome, sobrenome, registro_academico):
        self._nome = nome
        self._sobrenome = sobrenome
        self._registro_academico = registro_academico
         
    def imprimir(self):
        print("\nDados do aluno:")
        print(f"Nome: {self._nome} {self._sobrenome}, Registro Acadêmico: {self._registro_academico}")
    
    def set_nome(self, nome):
        self._nome = nome  # Permite alterar o nome
        print(f"\nO novo nome do aluno é: {self._nome}")  # Mensagem ao alterar

    def set_sobrenome(self, sobrenome):
        self._sobrenome = sobrenome  # Permite alterar o sobrenome
        print(f"O novo sobrenome do aluno é: {self._sobrenome}")  # Mensagem ao alterar

    def set_registro_academico(self, registro_academico):
        self._registro_academico = registro_academico  # Permite alterar o registro acadêmico
        print(f"O novo registro acadêmico do aluno é: {self._registro_academico}")  # Mensagem ao alterar
        
    def get_nome(self):
        return self._nome  # Retorna o nome

    def get_sobrenome(self):
        return self._sobrenome  # Retorna o sobrenome

    def get_registro_academico(self):
        return self._registro_academico  # Retorna o registro acadêmico

# Criando um objeto da classe Aluno
aluno = Aluno("Avril", "Stihler", "20241002")
aluno.imprimir()

# Alterando atributos usando os métodos set
aluno.set_nome("Gabriel")
aluno.set_sobrenome("Montresor")
aluno.set_registro_academico("20241003")

# Imprimindo novamente para ver as alterações
print("\nApós as alterações:")
aluno.imprimir()
