import re
import os

def valida_data(data):
    pattern = re.compile(r"\d\d/\d\d/\d\d\d\d", re.IGNORECASE)
    return pattern.match(data)

def criar_usuario(cpf):
  nome = input("Por favor, informe-nos seu nome: ")
  while True:
    data_nascimento = input("Agora, sua data de nascimento, no formato DD/MM/AAAA: ")
    if not valida_data(data_nascimento):
      print("Por favor, informe-nos uma data válida")
    else: break
  logradouro = input("Agora, o seu logradouro: ")
  while True:
    numero = input("O número da residência: ")
    if not numero.isdigit():
      print("Por favor, forneça um número válido!")
    else: break
  bairro = input("O nome do bairro da residência: ")
  cidade = input("O nome da cidade: ")
  while True:
    estado = input("A sigla do estado: ")
    if len(estado) != 2:
      print("Por favor, forneça uma sigla válida")
    else: break
  
  novo_usuario = {
    "nome": nome,
    "data_nascimento": data_nascimento,
    "endereco": f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}',
  }
  usuarios[cpf] = novo_usuario

  print("Usuário criado com sucesso!")
  return novo_usuario

def criar_conta_corrente(cpf_usuario):
  while True:
    senha = input("Por favor, informe uma senha para sua conta (até 6 dígitos): ")
    if len(senha) > 6 or not senha.isdigit():
      print("Informe uma senha válida!")
    else: break
  
  nova_conta = {
    "saldo": 0,
    "saques_dia": 0,
    "extrato": [],
    "senha": senha,
    "detentor": cpf_usuario,
  }
  
  contas[len(contas) + 1] = nova_conta
  return (nova_conta, len(contas))

def formatar_cpf(cpf):
  return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9::]}'

def saque_dinheiro(conta, valor):
  if valor <= 0:
    print("Não foi possível realizar o saque: valor inválido!")
  elif conta["saques_dia"] >= LIMITE_NUM_SAQUES:
    print("Não foi possível realizar o saque: limite diário de saques alcançado!")
  elif valor >= LIMITE_VALOR_SAQUE:
    print("Não foi possível realizar o saque: valor máximo de saque excedido!")
  elif valor > conta["saldo"]:
    print("Não foi possível realizar o saque: saldo insuficiente!")
  else:
    print("Realizando saque...")
    conta["saldo"] -= valor
    conta["saques_dia"] += 1
    conta["extrato"].append({
      "tipo_operacao": "saque",
      "valor": valor
    })
    print("Saque realizado com sucesso!")
  
  return conta

def deposito_dinheiro(conta, valor):
  if valor <= 0:
    print("Não foi possível realizar o depósito: valor inválido!")
  else:
    print("Realizando depósito...")
    conta["saldo"] += valor
    conta["extrato"].append({
      "tipo_operacao": "depósito",
      "valor": valor
    })
    print("Depósito realizado com sucesso!")
  
  return conta

def visualizar_extrato(saldo, extrato):
  print(f"Seu saldo bancário é de R${format(saldo, '.2f')}")
  print(f"Extrato: ")
  for op in extrato:
    print(f"{op['tipo_operacao'].capitalize()} - {op['valor']}")
  if len(extrato) == 0:
    print("Seu extrato do dia está vazio...")

def renderizar_menu(nome, num_conta):
  os.system('clear')
  print(f'''
{"PY-BANK".center(40, "-")}
Agência: {AGENCIA}
Conta: {num_conta}
Bem vindo ao Py-Bank, {nome}! O que deseja fazer?

[1] => Depósito
[2] => Saque
[3] => Ver extrato
[4] => Criar nova conta-corrente
[0] => Sair
  ''')

def main():
  print(f'''
{"PY-BANK".center(40, "-")}
Por favor, identifique-se!
  ''')

  while True:
    cpf = input("Seu CPF (somente números!): ")
    if not cpf.isdigit() or len(cpf) != 11:
      print("CPF inválido! Por favor digite novamente!")
    else:
      cpf = formatar_cpf(cpf)
      break

  if not cpf in usuarios:
    print("Parece que o seu CPF não está cadastrado no sistema, gostaria de se cadastrar como novo usuário?")
    while True:
      resp = input("[s/n]: ")
      if resp != 's' and resp != 'n':
        print("Informe uma opção válida")
      elif resp == 's':
        usuario = criar_usuario(cpf)
        break
      else:
        print("Agradecemos a preferência, volte sempre!")
        break
  else:
    usuario = usuarios[cpf]
  
  os.system('clear')
  if cpf in usuarios:
    print(f'''
{"PY-BANK".center(40, "-")}
Digite o número da sua conta abaixo, ou 0 se ainda não possui uma conta para criá-la.
    ''')

    while True:
      num_conta = int(input("Número: "))
      if num_conta < 0:
        print("Por favor, escolha uma opção válida!")
      elif num_conta == 0:
        (usuario["conta_ativa"], num_conta) = criar_conta_corrente(cpf)
        break
      elif (not num_conta in contas) or (num_conta in contas and contas[num_conta]["detentor"] != cpf):
        print("Desculpe, não encontramos uma conta com esse número, digite novamente o número da conta ou 0 para criar uma nova.")
      else:
        usuario["conta_ativa"] = contas[num_conta]
        break
    
    senha = input("Por favor, informe a senha da sua conta para acessá-la: ")

    if senha == usuario["conta_ativa"]["senha"]:
      renderizar_menu(usuario["nome"], num_conta)

      while True:
        while True:
          opcao = input("Sua opção: ")
          if opcao != '0' and opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
            print("Digite uma opção válida!")
          else: break

        opcao = int(opcao)

        if opcao == 1:
          while True:
            valor_deposito = input("Digite qual valor deseja depositar: ")
            if not valor_deposito.isdigit():
              print("Digite um número válido!")
            else: break
          
          usuario["conta_ativa"] = deposito_dinheiro(usuario["conta_ativa"], int(valor_deposito))

        elif opcao == 2:
          while True:
            valor_saque = input("Digite qual valor deseja sacar: ")
            if not valor_saque.isdigit():
              print("Digite um número válido!")
            else: break

          usuario["conta_ativa"] = saque_dinheiro(conta=usuario["conta_ativa"], valor=int(valor_saque))

        elif opcao == 3:
          visualizar_extrato(usuario["conta_ativa"]["saldo"], extrato=usuario["conta_ativa"]["extrato"])
        
        elif opcao == 4:
          (nova_conta, num_nova_conta) = criar_conta_corrente(cpf)
          while True:
            resp = input("Deseja utilizar a conta nova agora? [s/n]: ")
            if resp != 's' and resp != 'n':
              print("Por favor, informe uma opção válida!")
            elif resp == 's':
              usuario["conta_ativa"] = nova_conta
              renderizar_menu(usuario["nome"], num_nova_conta)
              break
            else: break

        elif opcao == 0:
          break
    
      print("Obrigado por usar o Py-Bank, ficamos felizes em tê-lo como cliente!")
    else:
      print("Senha incorreta, encerrando...")

usuarios = {
  "000.000.000-00": {
    "nome": "Teste da Silva Sauro",
    "data_nascimento": "31/02/1500",
    "endereco": "Rua Jefferson, 115 - Libélula - Araçapuca da Terra/MS",
  },
}
contas = {
  1: {
    "saldo": 1000,
    "saques_dia": 0,
    "extrato": [],
    "senha": "000000",
    "detentor": "000.000.000-00",
  },
}
LIMITE_NUM_SAQUES = 3
LIMITE_VALOR_SAQUE = 500
AGENCIA = "0001"

os.system('clear')

main()