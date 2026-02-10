class Celular:
    def __init__(self, marca, cor, modelo, custo, acessorios, armazenamento, bateria = 100, ligando=True, desligando=False, tocando=True):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.custo = custo
        self.acessorios = acessorios
        self.armazenamento = armazenamento
        self.bateria = bateria
        self.ligando = ligando
        self.desligando = desligando
        self.tocando = tocando

    def ligar(self):
        if self.ligando == True:
            print(f'Já esta ligado')
        else:
            self.ligando = True
            print('Começou a ligar')

    def desligar(self):
        if self.desligando == True:
            print(f'Já esta desligando')
        else:
            self.desligando = True
            print('Desligando')

    def tocar(self):
        if self.tocando == True:
            print("Já esta tocando")
        else:
            self.tocando = True
            print('Tocando')

    def usar_cel(self):
        if self.ligado == True:
            if self.bateria == 100:
                self.bateria = self.bateria - 10
            else:
                self.bateria = 0
                self.ligando = False
                f'Desligando... '
        else:
            f'Celular desligado'

    def apresentar(self):
        print(f'Marca: {self.marca}')
        print(f'Cor: {self.cor}')
        print(f'Modelo: {self.modelo}')
        print(f'Custo: {self.custo}')
        print(f'Acessorios: {self.acessorios}')
        print(f'Armazenamento: {self.armazenamento}')
        print(f'Bateria: {self.bateria}')
        print(f'Ligando: {self.ligando}')
        print(f'Desligando: {self.desligando}')
        print(f'Tocando: {self.tocando}')
        print("-" * 20)

cel1 = Celular("Iphone", "Branco", "bhhk", "R$1000", "Pelicula", "64G", 100, True, False, True)
cel2 = Celular("Sansung", "Preto", "asds", "R$50", "Pelicula", "32G", 100 , False, True, False)

cel1.apresentar()
cel2.apresentar()
