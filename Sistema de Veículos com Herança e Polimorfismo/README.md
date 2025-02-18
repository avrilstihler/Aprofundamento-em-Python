# Sistema de Veículos com Herança e Polimorfismo

Este projeto é uma implementação básica de um sistema de veículos em Python, demonstrando os conceitos de **herança**, **polimorfismo**, e **composição de classes**. Ele inclui classes que representam veículos, motores, e variações de carros, incluindo carros elétricos.

---

## Estrutura do Código

### Classes Principais

1. **`Veiculo`**  
   Classe base que representa um veículo genérico.  
   - **Atributos**: `marca`, `modelo`, `ano`, `velocidade`.  
   - **Métodos**: 
     - `mover()`: Verifica se o veículo está em movimento.
     - `parar()`: Para o veículo.

2. **`Motor`**  
   Classe que representa o motor de um veículo.  
   - **Atributos**: `tipo`, `potencia`.  
   - **Métodos**: 
     - `ligar()`: Liga o motor.
     - `desligar()`: Desliga o motor.

3. **`Carro`**  
   Subclasse de `Veiculo` que adiciona atributos e métodos específicos para carros.  
   - **Atributos**: `numero_de_portas`, `motor`.  
   - **Métodos**: 
     - Sobrescrita de `mover()`: Inclui informações sobre as portas.
     - `abrir_porta()`: Simula a abertura de uma porta.

4. **`CarroEletrico`**  
   Subclasse de `Carro` que representa carros elétricos.  
   - **Atributos**: `autonomia`.  
   - **Métodos**: 
     - Sobrescrita de `mover()`: Indica o movimento silencioso dos carros elétricos.
     - `carregar_bateria()`: Simula o carregamento da bateria.

---

## Exemplos de Uso

### Criando e Usando um Carro
```python
motor_carro = Motor(tipo="V8", potencia=450)
carro = Carro(marca="Ford", modelo="Mustang", ano=2022, numero_de_portas=2, motor=motor_carro)

carro.motor.ligar()
carro.mover()  # O carro está parado
carro.velocidade = 120
carro.mover()  # O carro está em movimento
carro.parar()
carro.motor.desligar()
```

### Criando e Usando um Carro Elétrico
```python
motor_eletrico = Motor(tipo="Elétrico", potencia=300)
carro_eletrico = CarroEletrico(marca="Tesla", modelo="Model S", ano=2023, numero_de_portas=4, motor=motor_eletrico, autonomia=600)

carro_eletrico.motor.ligar()
carro_eletrico.carregar_bateria()
carro_eletrico.velocidade = 80
carro_eletrico.mover()  # O carro elétrico está se movendo silenciosamente
carro_eletrico.parar()
carro_eletrico.motor.desligar()
```
## Exemplo de Saída
```plaintext
O motor V8 de 450 cavalos foi ligado.
O carro Ford Mustang está parado.
O carro Ford Mustang com 2 portas está se movendo a 120 km/h.
O veículo Ford Mustang parou.
Uma das 2 portas do carro Ford Mustang foi aberta.
O motor V8 de 450 cavalos foi desligado.

--- Carro Elétrico ---
O motor Elétrico de 300 cavalos foi ligado.
O carro elétrico Tesla Model S está carregando a bateria para 600 km de autonomia.
O carro elétrico Tesla Model S está se movendo silenciosamente a 80 km/h.
O veículo Tesla Model S parou.
O motor Elétrico de 300 cavalos foi desligado.
```
## Recursos Demonstrados
- Herança: Carro herda de Veiculo e CarroEletrico herda de Carro.
- Polimorfismo: Métodos como mover() são sobrescritos para se adaptarem ao comportamento específico de cada subclasse.
- Composição: Carro e CarroEletrico possuem um atributo motor, que é uma instância da classe Motor.

