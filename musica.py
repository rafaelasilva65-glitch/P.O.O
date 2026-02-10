class Musica:
    def __init__(self, nome, genero, cantor, estilo, gravadora, tocando=True, pausando=False, continuando=True):
        self.nome = nome
        self.genero = genero
        self.cantor = cantor
        self.estilo = estilo
        self.gravadora = gravadora
        self.tocando = tocando
        self.pausando = pausando
        self.continuando = continuando

    def tocar(self):
        if self.tocando == True:
            print('Já esta tocando')
        else:
            self.tocando = True
            print('Tocando')

    def pausar(self):
        if self.pausando == True:
            print('Já esta pausado')
        else:
            self.pausando = True
            print('Pausado')

    def continuar(self):
        if self.continuando == True:
            print(' Já esta continuando')
        else:
            self.continuando = True
            print('Continuando')

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Genero: {self.genero}')
        print(f'Cantor: {self.cantor}')
        print(f'Estilo: {self.estilo}')
        print(f'Gravadora: {self.gravadora}')
        print(f'Tocando: {self.tocando}')
        print(f'Pausando: {self.pausando}')
        print(f'Continuando: {self.continuando}')
        print("-" * 20)

mus1 = Musica("asdjiasd", "ashdujsad", "skdsud", "sdksdn", "skasdsdax", True, False, True)
mus2 = Musica("jnjsaks", "sjdasdsdw", "lksdad", "sodasjds", "skdasdassds", False, True, False)

mus1.apresentar()
mus2.apresentar()


