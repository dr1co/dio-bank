import re

def valida_data(data):
    pattern = re.compile(r"\d\d/\d\d/\d\d\d\d", re.IGNORECASE)
    return pattern.match(data)

def criar_usuario(cpf):
  nome = input("  Por favor, informe-nos seu nome: ")
  while True:
    data_nascimento = input("  Agora, sua data de nascimento, no formato DD/MM/AAAA: ")
    if not valida_data(data_nascimento):
      print("  Por favor, informe-nos uma data válida")
    else: break
  logradouro = input("  Agora, o seu logradouro: ")
  while True:
    numero = input("  O número da residência: ")
    if not numero.isdigit():
      print("  Por favor, forneça um número válido!")
    else: break
  bairro = input("  O nome do bairro da residência: ")
  cidade = input("  O nome da cidade: ")
  while True:
    estado = input("  A sigla do estado:")
    if len(estado) != 2:
      print("Por favor, forneça uma sigla válida")
    else: break
  
  novo_usuario = {
    "nome": nome,
    "data_nascimento": data_nascimento,
    "endereco": f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}',
  }
  usuarios[cpf] = novo_usuario

  print("  Usuário criado com sucesso!")

def criar_conta_corrente(agencia, num_conta, cpf_usuario):
  pass

def formatar_cpf(cpf):
  return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9::]}'

def saque_dinheiro(saldo, valor, saques_dia):
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

def deposito_dinheiro(saldo, valor):
  if valor <= 0:
    print("  Não foi possível realizar o depósito: valor inválido!")
  else:
    print("  Realizando depósito...")
    saldo += valor
    print("  Depósito realizado com sucesso!")
  
  return saldo

def visualizar_extrato(saldo, extrato):
  print(f"  Seu saldo bancário é de R${format(saldo, '.2f')}")

usuarios = {
  "000.000.000-00": {
    "nome": "Teste da Silva Sauro",
    "data_nascimento": "31/02/1500",
    "endereco": "Rua Jefferson, 115 - Libélula - Araçapuca da Terra/MS",
  },
}
contas = {
  1: {
    "saldo": 1000.00,
    "saques_dia": 0,
    "extrato": {},
    "detentor": "000.000.000-00"
  },
}
LIMITE_NUM_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
AGENCIA = "0001"

print(f'''
  {"DIO-BANK".center(40, "-")}
  Por favor, identifique-se!
''')

menu = f'''
  {"DIO-BANK".center(40, "-")}
  Bem vindo ao Dio-Bank, {nome}! O que deseja fazer?

  [1] => Depósito
  [2] => Saque
  [3] => Ver extrato
  [4] => Criar nova conta-corrente
  [0] => Sair
'''

while True:
  cpf = input("  Seu CPF: ")
  if not cpf.isdigit() and len(cpf) != 11:
    print("  CPF inválido! Por favor digite novamente!")
  else:
    cpf = formatar_cpf(cpf)
    break

if usuarios.index(cpf) == -1:
  print("  Parece que o seu CPF não está cadastrado no sistema, gostaria de se cadastrar como novo usuário?")
  resp = input("  [S/N]: ")
  if resp == 'S':
    usuario = criar_usuario(cpf)

print(menu)

while True:
  while True:
    opcao = input("  Sua opção: ")
    if opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
      print("  Digite uma opção válida!")
    else: break

  opcao = int(opcao)

  if opcao == 1:
    while True:
      valor_deposito = input("  Digite qual valor deseja depositar: ")
      if not valor_deposito.isdigit():
        print("  Digite um número válido!")
      else: break
    
    saldo = deposito_dinheiro(saldo, int(valor_deposito))

  elif opcao == 2:
    while True:
      valor_saque = input("  Digite qual valor deseja sacar: ")
      if not valor_saque.isdigit():
        print("  Digite um número válido!")
      else: break

    (saldo, saques_dia) = saque_dinheiro(saldo=saldo, valor_saque=int(valor_saque), saques_dia=saques_dia)

  elif opcao == 3:
    visualizar_extrato(saldo, extrato=extrato)

  elif opcao == 0:
    print("  Obrigado por usar o Dio-Bank, ficamos felizes em tê-lo como cliente!")
    break