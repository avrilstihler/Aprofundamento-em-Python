# Sistema de Monitoramento de Evasão Escolar

Este é um sistema simples para monitorar o desempenho acadêmico e a frequência dos alunos, ajudando a identificar **riscos de evasão escolar**. Ele utiliza conceitos de **Programação Orientada a Objetos (POO)** para encapsular dados e funcionalidades.

---

## Funcionalidades

1. **Cadastro de Alunos**:
   - Registro de nome, frequência e notas dos alunos.

2. **Monitoramento de Desempenho**:
   - Cálculo da média das notas.
   - Verificação de risco de evasão com base na frequência e no desempenho acadêmico.

3. **Identificação de Evasão**:
   - Determina se um aluno está em risco de evasão escolar com base em critérios predefinidos.

---

## Estrutura do Código

### Classe `Aluno`
Representa os dados básicos de um aluno.

- **Atributos**:
  - `nome`: Nome do aluno.
  - `notas`: Lista de notas obtidas pelo aluno.
  - `frequencia`: Frequência do aluno em porcentagem.

---

### Classe `Monitoramento`
Monitora o desempenho e a frequência do aluno.

- **Atributos**:
  - `aluno`: Um objeto da classe `Aluno`.

- **Métodos**:
  - `calcular_media()`: Calcula a média das notas do aluno.
  - `verificar_risco()`: Verifica se o aluno está em risco de evasão com base:
    - Frequência menor que 75%.
    - Média das notas menor que 7.0.

---

### Classe `Evasao`
Avalia se um aluno está em risco de evasão com base no monitoramento.

- **Atributos**:
  - `monitoramento`: Um objeto da classe `Monitoramento`.

- **Métodos**:
  - `verificar_evasao()`: Retorna `True` se o aluno estiver em risco de evasão.

---

## Como Usar

1. Execute o programa.
2. Insira os dados do aluno:
   - Nome.
   - Frequência (%).
   - Notas (separadas por espaço).
3. Escolha adicionar mais alunos ou finalizar o cadastro.
4. O sistema exibirá os resultados:
   - Média das notas.
   - Frequência.
   - Status de risco de evasão.

---

## Exemplos de Uso

### Entrada
```plaintext
=== Sistema de Monitoramento de Evasão Escolar ===

Digite os dados do aluno:
Nome do aluno: Ana
Frequência do aluno (%): 80
Notas do aluno (separe por espaços): 8.0 9.0 7.5

Deseja adicionar outro aluno? (s/n): s

Digite os dados do aluno:
Nome do aluno: João
Frequência do aluno (%): 70
Notas do aluno (separe por espaços): 5.0 6.0 6.5

Deseja adicionar outro aluno? (s/n): n
````
### Saída
````plaintext

=== Resultados ===

Aluno: Ana
Frequência: 80.0%
Média das Notas: 8.17
Risco de Evasão: Não

Aluno: João
Frequência: 70.0%
Média das Notas: 5.83
Risco de Evasão: Sim
````

Este projeto é útil para instituições de ensino que desejam monitorar e prevenir a evasão escolar, identificando alunos que precisam de suporte adicional. 🎓📊
