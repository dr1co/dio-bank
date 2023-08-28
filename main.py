def saqueDinheiro(saldo, valor, saques_dia):
  if valor <= 0:
    print("  Não foi possível realizar o saque: valor inválido!")
  elif saques_dia >= LIMITE_NUM_SAQUES:
    print("  Não foi possível realizar o saque: limite diário de saques alcançado!")
  elif valor >= LIMITE_VALOR_SAQUE:
    print("  Não foi possível realizar o saque: valor máximo de saque excedido!")
  elif valor > saldo:
    print("  Não foi possível realizar o saque: saldo insuficiente!")
  else:
    print("  Realizando saque...")
    saldo -= valor
    saques_dia += 1
    print("  Saque realizado com sucesso!")
  
  return (saldo, saques_dia)

def depositoDinheiro(saldo, valor):
  if valor <= 0:
    print("  Não foi possível realizar o depósito: valor inválido!")
  else:
    print("  Realizando depósito...")
    saldo += valor
    print("  Depósito realizado com sucesso!")
  
  return saldo

def visualizarExtrato(saldo):
  print(f"  Seu saldo bancário é de R${format(saldo, '.2f')}")

p_saldo = 1000.00
p_saques_dia = 0
LIMITE_NUM_SAQUES = 3
LIMITE_VALOR_SAQUE = 500


menu = f'''
  {"DIO-BANK".center(40, "-")}
  Bem vindo ao Dio-Bank! O que deseja fazer?

  [1] => Depósito
  [2] => Saque
  [3] => Ver extrato
  [0] => Sair
'''

print(menu)

while True:
  opcao = -1
  
  while opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3':
    opcao = input("  Sua opção: ")
    if opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3':
      print("  Digite uma opção válida!")

  opcao = int(opcao)

  if opcao == 1:
    valor_deposito = "a"

    while not valor_deposito.isdigit():
      valor_deposito = input("  Digite qual valor deseja depositar: ")
      if (not valor_deposito.isdigit()):
        print("  Digite um número válido!")
    
    p_saldo = depositoDinheiro(p_saldo, int(valor_deposito))

  elif opcao == 2:
    valor_saque = "a"
    
    while not valor_saque.isdigit():
      valor_saque = input("  Digite qual valor deseja sacar: ")
      if (not valor_saque.isdigit()):
        print("  Digite um número válido!")

    (p_saldo, p_saques_dia) = saqueDinheiro(p_saldo, int(valor_saque), p_saques_dia)

  elif opcao == 3:
    visualizarExtrato(p_saldo)

  elif opcao == 0:
    print("  Obrigado por usar o Dio-Bank, ficamos felizes em tê-lo como cliente!")
    break