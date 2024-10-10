print('ATIVO')
print('Soma (+)')
print('Subtração (-)')
print('Multiplicação (*)')
print('Divisão (/)')
Operação = input('Indique a operação desejada: ')
Número_1 = float(input('Selecione o primeiro termo: '))
Número_2 = float(input('Selecione o segundo termo: '))
if Operação == "+":
  Resultado = Número_1 + Número_2
  print(round(Resultado, 10))
elif Operação == "-":
  Resultado = Número_1 - Número_2
  print(round(Resultado, 10))
elif Operação == '*':
  Resultado = Número_1 * Número_2
  print(round(Resultado, 10))
elif Operação == '/':
  Resultado = Número_1 / Número_2
  print(round(Resultado, 10))
else:
  print(f"{Operação} não é um operador válido.")

# For foreigners, it's a simple calculator. :)
