class Aluno:
    def __init__(self, nome, idade, ano_nascimento, ano_atual, estudando, participando_atividade, fazendo_leitura):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = ano_nascimento
        self.ano_atual = ano_atual
        self.estudando = estudando
        self.participando_atividade = participando_atividade
        self.fazendo_leitura = fazendo_leitura

    def estudar(self):
        if self.estudando == True:
            print(f'Já esta estudando')
        else:
            self.estudando = True
            print('Estudando')

    def participar_atividade(self):
        if self.participando_atividade == True:
            print(f'Já esta participando de atividades')
        else:
            self.participando_atividade = True
            print('Participando da atividade')

    def fazer_leitura(self):
        if self.fazendo_leitura == True:
            print('Já esta fazendo a leitura')
        else:
            self.apredendo = True
            print('Fazendo a Leitura')

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Ano de nascimento: {self.ano_nascimento}')
        print(f'Ano atual: {self.ano_atual}')
        print(f'Estudando: {self.estudando}')
        print(f'participando_atividade: {self.participando_atividade}')
        print(f'fazendo_leitura: {self.fazendo_leitura}')
        print("-" * 20)


alu1 = Aluno("Rafael", "18", "11/12/07", "3 ano", True, False, True)
alu2 = Aluno("Rafael2", "19", "12/11/06", "3 ano", False, True, True)

alu1.apresentar()
alu2.apresentar()
