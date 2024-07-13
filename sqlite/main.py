from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classes.base import Base
from classes import Cliente
from classes import Conta

# Criação do banco de dados SQLite
engine = create_engine('sqlite:///sqlite_dio.db')

# Criação das tabelas no banco de dados
# Base.metadata.create_all(engine)

# Criação de uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Exemplos de inserção de dados
# novo_cliente = Cliente(nome='João Silva', cpf='12345678900', endereco='Rua A, 123')
# session.add(novo_cliente)
# session.commit()

# nova_conta = Conta(tipo='corrente', agencia='0001', numero='12345-6', id_cliente=novo_cliente.id, saldo=1000.0)
# session.add(nova_conta)
# session.commit()

# Consultando dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f'Cliente: {cliente.nome}, CPF: {cliente.cpf}')
    for conta in cliente.contas:
        print(f'Conta {conta.tipo}: {conta.agencia}-{conta.numero}, Saldo: {conta.saldo}')

# Fechando a sessão
session.close()
