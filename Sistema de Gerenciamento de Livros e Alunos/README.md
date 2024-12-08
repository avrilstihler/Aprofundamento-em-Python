# Sistema de Gerenciamento de Livros e Alunos

Este projeto implementa duas classes principais, **Livro** e **Aluno**, que demonstram conceitos básicos de **programação orientada a objetos (POO)**, como encapsulamento, getters, setters, e métodos de manipulação de dados.

---

## Estrutura do Código

### Classe `Livro`
A classe `Livro` representa um livro com informações básicas e métodos para exibir e alterar seus atributos.

- **Atributos**:
  - `_titulo`: O título do livro.
  - `_autor`: O autor do livro.
  - `_codigo_identificacao`: O código de identificação do livro.

- **Métodos**:
  - `imprimir()`: Exibe os dados do livro.
  - `set_titulo(titulo)`: Altera o título do livro.
  - `set_autor(autor)`: Altera o autor do livro.
  - `set_codigo_identificacao(codigo_identificacao)`: Altera o código de identificação do livro.
  - `get_titulo()`: Retorna o título do livro.
  - `get_autor()`: Retorna o autor do livro.
  - `get_codigo_identificacao()`: Retorna o código de identificação do livro.

### Classe `Aluno`
A classe `Aluno` representa um aluno com informações básicas e métodos para exibir e alterar seus atributos.

- **Atributos**:
  - `_nome`: O nome do aluno.
  - `_sobrenome`: O sobrenome do aluno.
  - `_registro_academico`: O registro acadêmico do aluno.

- **Métodos**:
  - `imprimir()`: Exibe os dados do aluno.
  - `set_nome(nome)`: Altera o nome do aluno.
  - `set_sobrenome(sobrenome)`: Altera o sobrenome do aluno.
  - `set_registro_academico(registro_academico)`: Altera o registro acadêmico do aluno.
  - `get_nome()`: Retorna o nome do aluno.
  - `get_sobrenome()`: Retorna o sobrenome do aluno.
  - `get_registro_academico()`: Retorna o registro acadêmico do aluno.

---

## Exemplos de Uso

### Manipulando um Livro
```python
# Criando um objeto da classe Livro
livro = Livro("O Ceifador", "Neal Shusterman", "1204")
livro.imprimir()

# Alterando atributos usando métodos set
livro.set_titulo("A Nuvem")
livro.set_autor("Neal Shusterman")
livro.set_codigo_identificacao("1205")

# Imprimindo novamente para verificar as alterações
print("\nApós as alterações:")
livro.imprimir()
````
### Manipulando um Aluno
````python

# Criando um objeto da classe Aluno
aluno = Aluno("Avril", "Stihler", "20241002")
aluno.imprimir()

# Alterando atributos usando métodos set
aluno.set_nome("Gabriel")
aluno.set_sobrenome("Montresor")
aluno.set_registro_academico("20241003")

# Imprimindo novamente para verificar as alterações
print("\nApós as alterações:")
aluno.imprimir()
````
## Exemplo de Saída
````python
Dados do livro:
Título: O Ceifador, Autor: Neal Shusterman, Código de Identificação: 1204

O novo título do livro é: A Nuvem
O novo autor do livro é: Neal Shusterman
O novo código de identificação do livro é: 1205

Após as alterações:
Dados do livro:
Título: A Nuvem, Autor: Neal Shusterman, Código de Identificação: 1205

Dados do aluno:
Nome: Avril Stihler, Registro Acadêmico: 20241002

O novo nome do aluno é: Gabriel
O novo sobrenome do aluno é: Montresor
O novo registro acadêmico do aluno é: 20241003

Após as alterações:

Dados do aluno:
Nome: Gabriel Montresor, Registro Acadêmico: 20241003
````
## Recursos Demonstrados
- **Encapsulamento:**
Uso de atributos privados (_atributo) para proteger os dados e métodos set e get para acessá-los e modificá-los.

- **Imutabilidade Controlada:**
Métodos set permitem a modificação controlada de atributos.

- **Facilidade de Extensão:**
O código é modular e pode ser facilmente estendido para suportar novas funcionalidades.


Explore o código para entender como usar getters, setters e a modularidade em aplicações POO! 📚👨‍🎓
