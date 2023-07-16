from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes =  []
        self.caixa = randint(11111111, 99999999)
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 10000000:
            print('Valor do caixa abaixo do nivel recomendado. Valor atual R${:,.2f}'.format(self.caixa))
        else:
            print('Valor do caixa acima do nivel recomentado. Valor atual R${:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print('R${:,.2f} Emprestado com sucesso, juros de R${:,.2f}'.format(valor, juros))
        else:
            print('Valor não disponivel em caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))






agencia1 = Agencia('818181818', 88888888, 99999)



agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(100011110, 12312123231123, 200)

agencia1.adicionar_cliente('hugo', 555555555, 100000)


