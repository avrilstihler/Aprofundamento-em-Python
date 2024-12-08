from planetas import planetas

def adicionar_planeta(): 
  nome = input('\nDigite o nome do planeta: ')
  tamanho = float(input('Digite o tamanho do planeta em km: '))
  distancia = float(input('Digite a distância do Sol em milhões de km: '))
  apelido = input('Digite o apelido deste planeta:  ')
  planetas[nome] = {'tamanho':  tamanho,  'distancia':  distancia,  'apelido':  apelido}
  print(f'O planeta {nome} foi adicionado com sucesso!')

def remover_planeta(): 
  nome = input('\nDigite o nome do planeta a ser removido: ')
  if nome in planetas: 
    del planetas[nome]
    print(f'O planeta {nome} foi removido com sucesso!')
  else: 
    print('Planeta não encontrado.')

def listar_planetas(): 
  if not planetas: 
    print('Não há planetas cadastrados.')
  else: 
    for planeta,  info in planetas.items(): 
      print(f'Planeta:  {planeta}')
      print(f'Tamanho:  {info["tamanho"]} km')
      print(f'Distância do Sol:  {info["distancia"]} milhões de km')
      print(f'Apelido:  {info["apelido"]}')
      print('-' * 40)

def buscar_planeta(): 
  nome = input('\nDigite o nome do planeta a ser buscado: ')
  if nome in planetas: 
    print(f'Planeta:  {nome}')
    print(f'Tamanho:  {planetas[nome]["tamanho"]} km')
    print(f'Distância do Sol:  {planetas[nome]["distancia"]} milhões de km')
    print(f'Apelido:  {planetas[nome]["apelido"]}')
    print('-' * 40)
  else: 
    print('Planeta não encontrado.')

def editar_planeta():
  nome = input("\nDigite o nome do planeta a ser editado: ")

  if nome in planetas:
    novo_tamanho = input("Digite o novo tamanho do planeta (ou deixe em branco para manter o atual): ")
    nova_distancia = input("Digite a nova distância do Sol (ou deixe em branco para manter a atual): ")
    novo_apelido = input("Digite o novo apelido do planeta (ou deixe em branco para manter o atual): ")

  if novo_tamanho:
    planetas[nome]['tamanho'] = novo_tamanho
  if nova_distancia:
    planetas[nome]['distancia'] = nova_distancia
  if novo_apelido:
    planetas[nome]['apelido'] = novo_apelido

    print(f"\nO planeta {nome} foi editado com sucesso!")
  else:
    print("Planeta não encontrado.")
