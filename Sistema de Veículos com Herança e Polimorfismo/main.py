class Veiculo:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def mover(self):
        if self.velocidade > 0:
            print(f"O veículo {self.marca} {self.modelo} está se movendo a {self.velocidade} km/h.")
        else:
            print(f"O veículo {self.marca} {self.modelo} está parado.")

    def parar(self):
        self.velocidade = 0
        print(f"O veículo {self.marca} {self.modelo} parou.")

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def ligar(self):
        print(f"O motor {self.tipo} de {self.potencia} cavalos foi ligado.")

    def desligar(self):
        print(f"O motor {self.tipo} de {self.potencia} cavalos foi desligado.")

# Classe Carro que herda de Veiculo e usa polimorfismo nos métodos
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas, motor, velocidade=0):
        super().__init__(marca, modelo, ano, velocidade)
        self.numero_de_portas = numero_de_portas
        self.motor = motor

    def mover(self):
        if self.velocidade > 0:
            print(f"O carro {self.marca} {self.modelo} com {self.numero_de_portas} portas está se movendo a {self.velocidade} km/h.")
        else:
            print(f"O carro {self.marca} {self.modelo} está parado.")

    def abrir_porta(self):
        print(f"Uma das {self.numero_de_portas} portas do carro {self.marca} {self.modelo} foi aberta.")

# Criando uma subclasse específica de Carro para mostrar polimorfismo
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, numero_de_portas, motor, autonomia, velocidade=0):
        super().__init__(marca, modelo, ano, numero_de_portas, motor, velocidade)
        self.autonomia = autonomia  # autonomia em km

    def mover(self):
        if self.velocidade > 0:
            print(f"O carro elétrico {self.marca} {self.modelo} está se movendo silenciosamente a {self.velocidade} km/h.")
        else:
            print(f"O carro elétrico {self.marca} {self.modelo} está parado.")

    def carregar_bateria(self):
        print(f"O carro elétrico {self.marca} {self.modelo} está carregando a bateria para {self.autonomia} km de autonomia.")

# Exemplo de uso
motor_carro = Motor(tipo="V8", potencia=450)
carro = Carro(marca="Ford", modelo="Mustang", ano=2022, numero_de_portas=2, motor=motor_carro)

motor_eletrico = Motor(tipo="Elétrico", potencia=300)
carro_eletrico = CarroEletrico(marca="Tesla", modelo="Model S", ano=2023, numero_de_portas=4, motor=motor_eletrico, autonomia=600)

# Demonstração de polimorfismo
carro.motor.ligar()
carro.mover()
carro.velocidade = 120
carro.mover()
carro.parar()
carro.abrir_porta()
carro.motor.desligar()

print("\n--- Carro Elétrico ---")
carro_eletrico.motor.ligar()
carro_eletrico.carregar_bateria()
carro_eletrico.velocidade = 80
carro_eletrico.mover()
carro_eletrico.parar()
carro_eletrico.motor.desligar()
