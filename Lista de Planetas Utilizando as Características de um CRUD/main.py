from crud import adicionar_planeta, remover_planeta, listar_planetas, buscar_planeta, editar_planeta

# Programa principal

fim = False
while not fim:
  print('Gerenciador de Planetas')
  print('1. Adicionar planeta')
  print('2. Remover planeta')
  print('3. Listar planetas')
  print('4. Buscar planeta')
  print('5. Editar planeta')
  print('0. Sair')

  opcao = input('\nDigite a opção desejada: ')

  if opcao == '1':
    adicionar_planeta()
  elif opcao == '2':
    remover_planeta()
  elif opcao == '3':
    listar_planetas()
  elif opcao == '4':
    buscar_planeta()
  elif opcao == '5':
    editar_planeta()
  elif opcao == '0':
    print('\nObrigado por utilizar nosso sistema!\n')
    fim = True
  else:
    print('\nOpção inválida.')
    
