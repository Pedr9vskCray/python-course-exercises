import csv
import os
import json
import xml.etree.ElementTree as xml
# atividade 6

class Empresa:
    def __init__(self, _id, nome, funcionarios, lucro):
        self._id = _id
        self.nome = nome
        self.funcionarios = funcionarios
        self.lucro = lucro

    @staticmethod
    def extrair_empresas():
        empresas = []
        with open("exercicio6.csv", "r") as text:
            myreader = csv.reader(text, delimiter=",")
            for info in myreader:
                if info[0] == "Id":
                    pass
                else:
                    temp = Empresa(info[0], info[1], info[2], info[3])
                    empresas.append(temp)
        return empresas

for empresa in Empresa.extrair_empresas():
    print(f"ID -> {empresa._id}")
    print(f"| Nome - {empresa.nome}")
    print(f"| N° de Funcionários - {empresa.funcionarios}")
    print(f"| Lucro Mensal - {empresa.lucro}\n")

# atividade 7

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    idPessoa = 1

    @staticmethod
    def salvar_funcionarios(*args):
        data = {}
        with open("exercício7.json", "w") as text:
            for info in args:
                data[f'Pessoa{Pessoa.idPessoa}'] = {
                    'nome': info.nome, 'idade': info.idade
                    }
                Pessoa.idPessoa += 1
            dumpData = json.dumps(data, ensure_ascii=False, indent=2)
            text.write(dumpData)
        return 1

pessoa1 = Pessoa('pedro', 19)
pessoa2 = Pessoa('thiago', 22)
pessoa3 = Pessoa('joão', 26)

#Pessoa.salvar_funcionarios(pessoa1, pessoa2, pessoa3)

# atividade 8

def extrair_info():
    array = []
    with open("exercício7.json", "rt") as text:
        arqv = text.read()
        data = json.loads(arqv)
        for key,value in data.items():
            temp = Pessoa(value['nome'], value['idade'])
            array.append(temp)
    return array

for pessoa in extrair_info():
    print(f"Nome: {pessoa.nome} - Idade: {pessoa.idade}")

print("\n")

# atividade 9

estados = ['Rio de Janeiro', 'Rio Grande do Sul', 'São Paulo']
rjCidades = ['Cabo Frio', 'Araruama', 'São Pedro da Aldeia', 'Rio de Janeiro']
rsCidades = ['Porto Alegre', 'Santa Maria', 'Gramado', 'Rio Grande']
spCidades = ['São Paulo', 'Osasco', 'Campinas', 'Guarulhos']


root = xml.Element("EstadosCidades")
rj = None
rs = None
sp = None
for estado in estados:
    match estado:
        case 'Rio de Janeiro':
            rj = xml.Element("Estado", attrib={"Nome": estado})
            for cidade in rjCidades:
                temp = xml.SubElement(rj, "Cidade")
                temp.text = cidade

        case 'Rio Grande do Sul':
            rs = xml.Element("Estado", attrib={"Nome": estado})
            for cidade in rsCidades:
                temp = xml.SubElement(rs, "Cidade")
                temp.text = cidade

        case 'São Paulo':
            sp = xml.Element("Estado", attrib={"Nome": estado})
            for cidade in spCidades:
                temp = xml.SubElement(sp, "Cidade")
                temp.text = cidade

for city in (rj, rs, sp):
    root.append(city)

arvore = xml.ElementTree(root)

with open("estados.xml", "wb") as text:
    arvore.write(text)