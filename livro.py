class Livro:
    def __init__(self, nome, data_public, autor, genero, editora, material, idioma, abrindo=True, fechando=False, lendo=True):
        self.nome = nome
        self.data_public = data_public
        self.autor = autor
        self.genero = genero
        self.editora = editora
        self.material = material
        self.idioma = idioma
        self.abrindo = abrindo
        self.fechando = fechando
        self.lendo = lendo

    def abrir(self):
        if self.abrindo == True:
            print(f'Já abrido')
        else:
            self.abrindo = True
            print('Aberto')

    def fechar(self):
        if self.fechando == True:
            print(f'Já fechado')
        else:
            self.fechando = True
            print('Fechado')

    def ler(self):
        if self.lendo == True:
            print(f'Já esta lendo')
        else:
            self.lendo = True
            print('Lendo')

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Data_public: {self.data_public}')
        print(f'Autor: {self.autor}')
        print(f'Genero: {self.genero}')
        print(f'Editora: {self.editora}')
        print(f'Material: {self.material}')
        print(f'Idioma: {self.idioma}')
        print(f'Abrindo: {self.abrindo}')
        print(f'Fechado: {self.fechando}')
        print(f'Lendo: {self.lendo}')
        print("-" * 20)

liv1 = Livro("sjdjasd", "12323", "asjdkasd", "sksdds", "sidjdas", "asjdasxd", "asdmsa", True, False, True)
liv2 = Livro("jiasdasd","389221", "sjdmaasd", "osadsd", "awpsdsadok", "wsdnasnd", False, True, False)

liv1.apresentar()
liv2.apresentar()