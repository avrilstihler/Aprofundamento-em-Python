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
