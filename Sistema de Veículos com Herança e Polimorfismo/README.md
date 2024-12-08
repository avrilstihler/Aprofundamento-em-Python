# Sistema de Veículos com Herança e Polimorfismo
Este projeto é uma implementação básica de um sistema de veículos em Python, demonstrando os conceitos de herança, polimorfismo, e composição de classes. Ele inclui classes que representam veículos, motores, e variações de carros, incluindo carros elétricos.

## Estrutura do Código
### Classes Principais
- Veiculo


Classe base que representa um veículo genérico.

-- Atributos: marca, modelo, ano, velocidade.
-- Métodos:

  
mover(): Verifica se o veículo está em movimento.


parar(): Para o veículo.
- Motor


Classe que representa o motor de um veículo.

Atributos: tipo, potencia.
Métodos:
ligar(): Liga o motor.
desligar(): Desliga o motor.
Carro
Subclasse de Veiculo que adiciona atributos e métodos específicos para carros.

Atributos: numero_de_portas, motor.
Métodos:
Sobrescrita de mover(): Inclui informações sobre as portas.
abrir_porta(): Simula a abertura de uma porta.
CarroEletrico
Subclasse de Carro que representa carros elétricos.

Atributos: autonomia.
Métodos:
Sobrescrita de mover(): Indica o movimento silencioso dos carros elétricos.
carregar_bateria(): Simula o carregamento da bateria.
Exemplos de Uso
O código demonstra a criação de objetos das classes e o uso de polimorfismo, herança e composição. Aqui estão alguns exemplos:

Criando e Usando um Carro
python
Copiar código
motor_carro = Motor(tipo="V8", potencia=450)
carro = Carro(marca="Ford", modelo="Mustang", ano=2022, numero_de_portas=2, motor=motor_carro)

carro.motor.ligar()
carro.mover()  # O carro está parado
carro.velocidade = 120
carro.mover()  # O carro está em movimento
carro.parar()
carro.motor.desligar()
Criando e Usando um Carro Elétrico
python
Copiar código
motor_eletrico = Motor(tipo="Elétrico", potencia=300)
carro_eletrico = CarroEletrico(marca="Tesla", modelo="Model S", ano=2023, numero_de_portas=4, motor=motor_eletrico, autonomia=600)

carro_eletrico.motor.ligar()
carro_eletrico.carregar_bateria()
carro_eletrico.velocidade = 80
carro_eletrico.mover()  # O carro elétrico está se movendo silenciosamente
carro_eletrico.parar()
carro_eletrico.motor.desligar()
Recursos Demonstrados
Herança: Carro herda de Veiculo e CarroEletrico herda de Carro.
Polimorfismo: Métodos como mover() são sobrescritos para se adaptarem ao comportamento específico de cada subclasse.
Composição: Carro e CarroEletrico possuem um atributo motor, que é uma instância da classe Motor.
Requisitos
Python 3.6 ou superior
O código usa a sintaxe moderna do Python, incluindo f-strings.
Explore o sistema e entenda como a programação orientada a objetos pode tornar seus projetos mais modulares e organizados! 🚗⚡
