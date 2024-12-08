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
