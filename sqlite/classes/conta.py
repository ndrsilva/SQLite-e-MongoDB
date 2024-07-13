from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


# Definição da tabela Conta
class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    numero = Column(String, nullable=False, unique=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Float, default=0.0)

    # Relacionamento muitos para um com a tabela Cliente
    cliente = relationship('Cliente', back_populates='contas')
