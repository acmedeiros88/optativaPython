from peewee import *
from Pessoa import Pessoa
from Endereco import Endereco
from BaseModel import *
import os


class Motorista(Pessoa):
    matricula = CharField()
    catCNH = CharField()

    def __str__(self):
        return super().__str__() + "Matricula: " + self.matricula + "CNH: " + self.catCNH


if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Endereco, Motorista])
    end = Endereco.create(cep=89035100, logradouro="Rua abc", numero=123,
                          bairro="Vila Nova", municipio="Blumenau", estado="SC")

    mot = Motorista.create(nome="Joao da silva", endereco=end, email="manda@gmail.com",
                           matricula="D001", catCNH="categoria D")
    print(mot)
