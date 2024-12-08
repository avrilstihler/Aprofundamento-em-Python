from abc import ABC, abstractmethod
import random
from datetime import datetime, timedelta

# Classe abstrata Pagamento
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

# Subclasse PagamentoCartao
class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao
    
    def validar_cartao(self):
        # Verifica se o número do cartão tem 16 dígitos e é numérico
        return len(self.numero_cartao) == 16 and self.numero_cartao.isdigit()

    def processar_pagamento(self, valor):
        if self.validar_cartao():
            print(f"🔔 Pagamento aprovado! Processando R${valor:.2f} com o cartão de crédito.")
            print("💳 Transação realizada com sucesso! Obrigado por usar nossos serviços.")
        else:
            print("❌ Número do cartão inválido. Por favor, verifique os dados e tente novamente.")

# Subclasse PagamentoBoleto
class PagamentoBoleto(Pagamento):
    def __init__(self):
        self.codigo_barras = None

    def gerar_boleto(self):
        # Gera um código de barras fictício de 47 dígitos
        self.codigo_barras = ''.join([str(random.randint(0, 9)) for _ in range(47)])
        validade = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
        print(f"📄 Boleto gerado! Código de barras: {self.codigo_barras}")
        print(f"🗓️  Data de vencimento: {validade}")
        return self.codigo_barras

    def processar_pagamento(self, valor):
        self.gerar_boleto()
        print(f"💰 Pagamento de R${valor:.2f} processado com boleto bancário.")
        print("🔔 Atenção: Pague seu boleto até a data de vencimento para evitar multas.")

# Criando um pagamento por cartão de crédito
print("=== Simulação de Pagamento com Cartão de Crédito ===")
pagamento_cartao = PagamentoCartao("1234567812345678")
pagamento_cartao.processar_pagamento(250.00)

print("\n=== Simulação de Pagamento com Boleto ===")
# Criando um pagamento por boleto
pagamento_boleto = PagamentoBoleto()
pagamento_boleto.processar_pagamento(400.00)
