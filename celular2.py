class Celular:
    def __init__(self, marca, modelo, bateria = 100, ligado=True):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = ligado


    def usar_cel(self):
        if self.ligado == True:
            if self.bateria >= 10:
                self.bateria = self.bateria - 10
                f'Bateria: {self.bateria}%'

