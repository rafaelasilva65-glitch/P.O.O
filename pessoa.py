class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True,Trabalhando=False, salario=0):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.Trabalhando = Trabalhando
        self.salario = salario

    def trabalhar(self):
        if self.trabalhando == True:
            print(f'Já esta trabalhando')
        else:
            self.trabalhando == True
            #salario
            self.salario = 1000
            print('Começou a trabalhar')

    def estudar(self, aumento=200):
        if self.estudando == True:
            print('Ja esta estudando')
            if self.trabalhando == True:
                self.salario= (self.salario + aumento)
                print(f'{self.nome} recebeu um aumento de R$200')
        else:
            self.estudando = True
            print('Estudando')


    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Codigo: {self.codigo}")
        print(f"Estudando: {self.estudando}")
        print(f"Trabalhando: {self.Trabalhando}")
        print("-" * 20)

p1 = Pessoa("Rafael", 2007, 9, True, False)
p2 = Pessoa('Rafael2', 2006, 8, False, True)
p3 = Pessoa('Rafael3', 2005, 7)
p4 = Pessoa('Rafael4', 2004, 6)
p5 = Pessoa('Rafael5', 2003, 5)

p1.apresentar()
p2.apresentar()
p3.apresentar()
p4.apresentar()
p5.apresentar()