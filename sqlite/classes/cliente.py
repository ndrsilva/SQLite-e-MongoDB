from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


# Definição da tabela Cliente
class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    endereco = Column(String)

    # Relacionamento um para muitos com a tabela Conta
    contas = relationship('Conta', back_populates='cliente')
