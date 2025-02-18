# Uso de Funções e Módulos Externos

Este é um programa que explora o uso de **funções** e **módulos externos** para realizar cálculos como **fatorial** e **somas (pares e ímpares)** de números fornecidos pelo usuário. Ele oferece uma interface interativa que permite consultar resultados para múltiplos números em sequência.

---

## Funcionalidades

1. **Cálculo do Fatorial**:
   - Calcula o produto de todos os números inteiros positivos até o número fornecido.

2. **Cálculo do Somatório**:
   - Soma os números pares ou ímpares de `0` até o número fornecido.

3. **Entrada Interativa**:
   - Permite ao usuário consultar os resultados para vários números.

4. **Uso de Módulos Externos**:
   - A lógica do cálculo é modularizada, podendo ser reutilizada em outros programas.

5. **Opção de Saída**:
   - Digite `-1` para encerrar o programa a qualquer momento.

---

## Estrutura do Código

### Funções no Módulo `minha_biblioteca.py`

#### `calcularFatorial(numero)`
- Calcula e retorna o fatorial de um número.
- **Parâmetros**:
  - `numero`: Número inteiro positivo.
- **Retorno**:
  - Fatorial do número fornecido.

#### `calcularSomatorio(numero, pares)`
- Calcula a soma dos números pares ou ímpares até o número fornecido.
- **Parâmetros**:
  - `numero`: Número inteiro positivo.
  - `pares`: Booleano que indica se a soma deve incluir apenas números pares (`True`) ou ímpares (`False`).
- **Retorno**:
  - Soma dos números pares ou ímpares até o número.

#### `exibirResultados(numero)`
- Exibe os resultados do fatorial e dos somatórios (pares e ímpares) para o número fornecido.
- **Parâmetros**:
  - `numero`: Número inteiro positivo.

---

### Arquivo Principal `programa_principal.py`

#### `main()`
- Controla o fluxo do programa.
- Solicita ao usuário a quantidade de números que deseja consultar.
- Processa cada número fornecido, exibindo os resultados ou encerrando caso `-1` seja digitado.

---

## Como Usar

1. **Estrutura de Arquivos**:
   - Crie dois arquivos:
     - `programa_principal.py` (arquivo principal para execução).
     - `minha_biblioteca.py` (contendo as funções mencionadas acima).

2. **Execute o programa**.
3. Informe a quantidade de números que deseja consultar.
4. Para cada número, digite o valor desejado.
   - O programa exibirá o fatorial, a soma dos pares e a soma dos ímpares.
5. Digite `-1` para encerrar o programa a qualquer momento.

---

## Exemplo de Uso

### Entrada
```plaintext
Quantos números deseja consultar? (Digite -1 para sair): 2
Informe o número 1: 5
Informe o número 2: 6
````
### Saída
````plaintext
O fatorial de 5 é: 120
A soma dos pares até 5 é: 6
A soma dos ímpares até 5 é: 9

O fatorial de 6 é: 720
A soma dos pares até 6 é: 12
A soma dos ímpares até 6 é: 9

Obrigado por utilizar o sistema!
