num1 = None
num2 = None
soma = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


num1 = float(text_prompt('Digite o primeiro número: '))
num2 = float(text_prompt('Digite o segundo número: '))
soma = num1 + num2
print(''.join([str(x) for x in ['A soma de ', num1, ' e ', num2, ' é igual a: ', soma]]))
