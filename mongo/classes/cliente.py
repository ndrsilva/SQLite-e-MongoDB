from mongoengine import Document, StringField, ReferenceField, ListField


# Definição da coleção Cliente
class Cliente(Document):
    nome = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    endereco = StringField()
    contas = ListField(ReferenceField('Conta'))
