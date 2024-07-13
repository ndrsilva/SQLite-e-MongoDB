from mongoengine import Document, StringField, FloatField, ReferenceField
from .cliente import Cliente


# Definição da coleção Conta
class Conta(Document):
    tipo = StringField(required=True)
    agencia = StringField(required=True)
    numero = StringField(required=True, unique=True)
    id_cliente = ReferenceField(Cliente, required=True)
    saldo = FloatField(default=0.0)
