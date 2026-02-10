class Maquiagem():
    def __init__(self, marca, categoria, material, validade, preco, duracao, textura, usando=True, removendo=False, trocando=True):
        self.marca = marca
        self.categoria = categoria
        self.material = material
        self.validade = validade
        self.preco = preco
        self.duracao = duracao
        self.textura = textura
        self.usando = usando
        self.removendo = removendo
        self.trocando = trocando

    def usar(self):
        if self.usando == True:
            print(f'Já esta usando')
        else:
            self.usando = True
            print('Usando')

    def remover(self):
        if self.removendo == True:
            print(f'Já esta removendo')
        else:
            self.removendo = True
            print('Removendo')

    def trocar(self):
        if self.trocando == True:
            print(f'Já esta trocando')
        else:
            self.trocando = True
            print('Trocando')

    def apresentar(self):
        print(f'Marca: {self.marca}')
        print(f'Categoria: {self.categoria}')
        print(f'Material: {self.material}')
        print(f'Validade: {self.validade}')
        print(f'Preco: {self.preco}')
        print(f'Duracao: {self.duracao}')
        print(f'Textura: {self.textura}')
        print(f'Usando: {self.usando}')
        print(f'Removendo: {self.removendo}')
        print(f'Trocando: {self.trocando}')
        print("-" * 20)

maq1 = Maquiagem("skdjashd", "dmdjfgsd", "pofejhrsnah", "jdisjadw", "R$75", "20h", "jshasdssw", True, False, True)
maq2 = Maquiagem("ksdkasde", "ksmsahdsmwi", "kdnnhcjfo", "lsiuduieuo", "R$30", "24h", "ksjmsaudw", False, True, False)

maq1.apresentar()
maq2.apresentar()