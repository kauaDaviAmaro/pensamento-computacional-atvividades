from os import system
# from IPython.display import clear_output

error = []

class Produto:
    
    def __init__(self, nome: str, preco: float, quantiMaxima: float, quantiMinima: float, descontoExtra: float,desconto: int = 20) -> None:
        self.nome = nome
        self.preco = preco
        self.quantiMaxima = quantiMaxima
        self.quantiMinima = quantiMinima
        self.descontoExtra = descontoExtra
        self.desconto = desconto

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
    def calcularDesconto(self, descontoDe10Por):
        valorTotal = self.calcularValorTotal()
        desconto = 0
        for produto, quanti in self.produtos:
            if produto.descontoExtra < quanti:
                desconto += (((produto.preco * quanti) * produto.desconto) / 100)
        if valorTotal > descontoDe10Por:
            desconto += valorTotal * 0.10
        return desconto

    # Entrga o valor com desconto
    def calcularValorComDesconto(self, descontoDe10Por: float):
        valorTotal = self.calcularValorTotal()
        valorTotal -= self.calcularDesconto(descontoDe10Por)
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
        # clear_output()
        system('cls')
        print(
            f'Insira as informações abaixo (Gerente): \n{"=="*20}\nInsira as informações do produto "{i}":\n')

        preco = float(input('Preço do produto: '))
        quantiMinima = int(input('Quantidade mínima do produto: '))
        quantiMaxima = int(input('Quantidade máxima do produto: '))
        decontoApartir = float(input('desconto de 20% apartir: '))
        prodLista.append(Produto(i, preco, quantiMaxima,
                         quantiMinima, decontoApartir))

    return prodLista

# Configurar produtos (cliente)


def lerProdutosCliente(produtos: Produto) -> None:
    carrinho = CarrinhoDecompras()
    for i in produtos:
        system('cls')
        print(
            f'Insira as informações abaixo (Cliente): \n{"=="*20}\nInsira as informações do produto "{i.nome}":\nPreço={i.preco}\nMaximo={i.quantiMaxima}\nMinima={i.quantiMinima}\nDesconto a partir de {i.descontoExtra}')
        # clear_output()

        quantidade = int(input('Insira a quantidade da compra : '))
        carrinho.colocarItem(i, quantidade)

    return carrinho


listaProdutos = {
    'Contra-filé',
    'Lata de cerveja',
}

prod = lerProdutosGerente(listaProdutos)

descontoDe10Porce = float(input('A partir de qual total a compra tem mais 10% de desconto: '))

carrinhoCompras = lerProdutosCliente(prod)

system('cls')
if error != []:
    print('Durante a execução foram encontrados os seguinte(s) erro(s): ')
    for i in error:
        print(i)

print(f'''
Pagamento
{"="*15}
Valor Total: R$ {carrinhoCompras.calcularValorTotal():.2f}
Desconto: R$ {carrinhoCompras.calcularDesconto(descontoDe10Porce):.2f}
Valor com desconto: R$ {carrinhoCompras.calcularValorComDesconto(descontoDe10Porce):.2f}
''')
