class Time:
    def __init__(self, jogador, treino, tecnico, estadio, patrocinador, cor, jogando=True, treinando=False, divertindo=True):
        self.jogador = jogador
        self.treino = treino
        self.tecnico = tecnico
        self.estadio = estadio
        self.patrocinador = patrocinador
        self.cor = cor
        self.jogando = jogando
        self.treinando = treinando
        self.divertindo = divertindo

    def jogar(self):
        if self.jogando == True:
            print(f'Já esta jogando')
        else:
            self.jogando = True
            print('Jogando')

    def treinar(self):
        if self.treinando == True:
            print(f'Já esta treinando')
        else:
            self.treinando = True
            print('Treinando')

    def divertir(self):
        if self.divertindo == True:
            print(f'Já esta divertindo')
        else:
            self.divertindo = True
            print('Divertindo')

    def apresentar(self):
        print(f'Jogador {self.jogador}')
        print(f'Treino {self.treino}')
        print(f'Tecnico {self.tecnico}')
        print(f'Estadio {self.estadio}')
        print(f'Patrocinador {self.patrocinador}')
        print(f'Cor: {self.cor}')
        print(f'Jogando: {self.jogando}')
        print(f'Treinando: {self.treinando}')
        print(f'Divertindo: {self.divertindo}')
        print("-" * 20)

tim1 = Time("sjhdasd", "sijdjasd", "jsdnjasd", "ksadasdasdasd", "osdkasdmxs", "smdkasdwas", True, False, True)
tim2 = Time("sdnjasd", "jchasdjwokdl", "ncmsudws", "ldkjfheirm", "jsdsjdjnaudjmsc", "mkvoraswc", False, True, False)

tim1.apresentar()
tim2.apresentar()