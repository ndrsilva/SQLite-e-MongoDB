from pymongo import MongoClient
from mongoengine import connect
from classes import Cliente
from classes import Conta

# # Conexão com o MongoDB no Docker
# client = MongoClient('mongodev://localhost:27017/')

# Conexão com o banco de dados MongoDB
connect('mongodev', host='localhost', port=27017)

# Exemplos de inserção de dados
# novo_cliente = Cliente(nome='João Silva', cpf='12345678900', endereco='Rua A, 123')
# novo_cliente.save()

# nova_conta = Conta(tipo='corrente', agencia='0001', numero='12345-6', id_cliente=novo_cliente, saldo=1000.0)
# nova_conta.save()

# Atualizando o campo 'contas' do Cliente
# novo_cliente.contas.append(nova_conta)
# novo_cliente.save()

# Consultando dados
clientes = Cliente.objects()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}, CPF: {cliente.cpf}')
    for conta in cliente.contas:
        print(f'Conta {conta.tipo}: {conta.agencia}-{conta.numero}, Saldo: {conta.saldo}')
