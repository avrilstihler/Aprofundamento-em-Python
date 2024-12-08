# Sistema de Pagamentos em Python

Este projeto é uma implementação simples de um sistema de pagamentos que utiliza conceitos de **programação orientada a objetos** em Python, incluindo **classes abstratas**, **herança**, e **métodos abstratos**. O sistema suporta dois métodos de pagamento: **cartão de crédito** e **boleto bancário**.

---

## Estrutura do Código

### Classes Principais

1. **`Pagamento` (Classe Abstrata)**  
   Representa a base para diferentes métodos de pagamento.  
   - **Métodos**: 
     - `processar_pagamento(valor)`: Método abstrato que deve ser implementado pelas subclasses.

2. **`PagamentoCartao`**  
   Implementa o pagamento via cartão de crédito.  
   - **Atributos**: 
     - `numero_cartao`: Número do cartão de crédito.  
   - **Métodos**: 
     - `validar_cartao()`: Verifica se o número do cartão é válido.
     - `processar_pagamento(valor)`: Processa o pagamento se o cartão for válido.

3. **`PagamentoBoleto`**  
   Implementa o pagamento via boleto bancário.  
   - **Atributos**: 
     - `codigo_barras`: Código de barras gerado para o boleto.  
   - **Métodos**: 
     - `gerar_boleto()`: Gera um código de barras fictício e exibe a data de vencimento.
     - `processar_pagamento(valor)`: Processa o pagamento e gera o boleto.

---

## Exemplos de Uso

### Pagamento com Cartão de Crédito
```python
# Criando um pagamento com cartão de crédito
print("=== Simulação de Pagamento com Cartão de Crédito ===")
pagamento_cartao = PagamentoCartao("1234567812345678")
pagamento_cartao.processar_pagamento(250.00)
````
### Pagamento com Boleto Bancário
````python
# Criando um pagamento com boleto
print("\n=== Simulação de Pagamento com Boleto ===")
pagamento_boleto = PagamentoBoleto()
pagamento_boleto.processar_pagamento(400.00)
````
## Exemplo de Saída
````python
=== Simulação de Pagamento com Cartão de Crédito ===
🔔 Pagamento aprovado! Processando R$250.00 com o cartão de crédito.
💳 Transação realizada com sucesso! Obrigado por usar nossos serviços.

=== Simulação de Pagamento com Boleto ===
📄 Boleto gerado! Código de barras: 30495626862116749560295757872822502773313851482
🗓️  Data de vencimento: 15/12/2024
💰 Pagamento de R$400.00 processado com boleto bancário.
🔔 Atenção: Pague seu boleto até a data de vencimento para evitar multas.
````
## Recursos Demonstrados
- **Abstração e Herança:**
A classe *Pagamento* é abstrata e define o método *processar_pagamento*, obrigatório para as subclasses.
- **Polimorfismo:**
Subclasses *PagamentoCartao* e *PagamentoBoleto* implementam o método processar_pagamento de formas diferentes.
- **Geração de Dados Aleatórios:**
O código de barras do boleto é gerado aleatoriamente com 47 dígitos.
- **Validação de Dados:**
A classe *PagamentoCartao* verifica se o número do cartão é válido (16 dígitos e numérico).


Explore o sistema e veja como ele pode ser adaptado para diferentes cenários de pagamento no mundo real! 💳📄
