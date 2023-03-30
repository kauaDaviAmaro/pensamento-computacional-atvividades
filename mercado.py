from dataclasses import dataclass
from os import system
#from IPython.display import clear_output

error = []

@dataclass
class Produto:
    nome: str
    preco: float
    quantiMaxima: float
    quantiMinima: float
    descontoExtra: int
    desconto: int = 20

@dataclass
class CarrinhoDecompras:

    def __init__(self) -> None:
        self.produtos = []

    # Coloca itens na classe Carrinho
    def colocarItem(self, produto: Produto, quantidade: int) -> None:
        if quantidade > produto.quantiMaxima:
            error.append(f'Impossivel adicionar o produto "{produto.nome}": Valor acima da quantidade maxima de {produto.quantiMaxima}')
        elif quantidade < produto.quantiMinima:
            error.append(f'Impossivel adicionar o produto "{produto.nome}": Valor abaixo da quantidade minima de {produto.quantiMinima}')
        else:
            self.produtos.append((produto, quantidade))

    #entrega somente desconto
    def calcularDesconto(self):
        desconto = 0
        for produto, quanti in self.produtos:
            desconto += ((produto.preco * produto.desconto) / 100)
            if produto.descontoExtra != None:
                desconto += ((produto.preco * produto.descontoExtra) / 100)
        return desconto

    # Entrga o valor com desconto
    def calcularValorComDesconto(self): 
        valorTotal = self.calcularValorTotal()
        for produto, quanti in self.produtos:
            valorTotal -= ((produto.preco * produto.desconto) / 100)
            if produto.descontoExtra != None:
                valorTotal -= ((produto.preco * produto.descontoExtra) / 100)
        
        return valorTotal

    # Entrga o valor bruto
    def calcularValorTotal(self) -> float:
        valorTotal = 0
        for produto, quanti in self.produtos:
            valorTotal += produto.preco * quanti

        return valorTotal


# Configurar produtos (gerente)
def lerProdutosGerente(produtos: list) -> list:
    prodLista = []
    for i in produtos:
        #clear_output()
        system('cls')
        print(
            f'Insira as informações abaixo (Gerente): \n{"=="*20}\nInsira as informações do produto "{i}":\n')

        preco = float(input('Preço do produto: '))
        quantiMinima = int(input('Quantidade mínima do produto: '))
        quantiMaxima = int(input('Quantidade máxima do produto: '))
        descontoExtra = input('Desconto extra (s/n): ').lower()
        if descontoExtra in ['s', 'sim']:
            descontoExtra = float(input('Desconto extra: '))
        else:
            descontoExtra = None

        prodLista.append(Produto(i, preco, quantiMaxima,
                         quantiMinima, descontoExtra))

    return prodLista

# Configurar produtos (cliente)
def lerProdutosCliente(produtos: Produto) -> None:
    carrinho = CarrinhoDecompras()
    for i in produtos:
        #clear_output()
        system('cls')
        print(
            f'Insira as informações abaixo (Cliente): \n{"=="*20}\nInsira as informações do produto "{i.nome}":\nPreço={i.preco}\nMaximo={i.quantiMaxima}\nMinima={i.quantiMinima}')
        # clear_output()

        quantidade = int(input('Insira a quantidade da compra : '))
        carrinho.colocarItem(i, quantidade)

    return carrinho


listaProdutos = {
    'Contra-filé',
    'Lata de cerveja',
    'Pão de alho',
    'refrigerane',
    'carvao',
    'panceta'
}

prod = lerProdutosGerente(listaProdutos)
carrinhoCompras = lerProdutosCliente(prod)

#clear_output()
system('cls')
if error != []:
    print('Durante a execução foram encontrados os seguinte(s) erro(s): ')
    for i in error:
        print(i)
print(f'''
Pagamento
{"="*15}
Valor Total: R$ {carrinhoCompras.calcularValorTotal():.2f}
Desconto: R$ {carrinhoCompras.calcularDesconto():.2f}
Valor com desconto: R$ {carrinhoCompras.calcularValorComDesconto():.2f}
''')
