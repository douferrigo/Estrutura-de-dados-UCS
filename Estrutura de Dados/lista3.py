class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.proximo = None
        self.anterior = None

class ListaProdutos:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar_produto(self, nome, preco):
        novo_produto = Produto(nome, preco)
        if self.primeiro is None:
            self.primeiro = novo_produto
            self.ultimo = novo_produto
        else:
            novo_produto.anterior = self.ultimo
            self.ultimo.proximo = novo_produto
            self.ultimo = novo_produto

    def promocao(self):
        if self.primeiro is None:
            print("Não há produtos disponíveis.")
            return

        atual = self.primeiro
        while atual:
            segundo = atual.proximo
            while segundo:
                if atual.preco + segundo.preco == 7:
                    if atual.preco > segundo.preco:
                        print(f"Promoção: Compre {segundo.nome} e ganhe desconto no {atual.nome}.")
                    else:
                        print(f"Promoção: Compre {atual.nome} e ganhe desconto no {segundo.nome}.")
                segundo = segundo.proximo
            atual = atual.proximo

# Criando alguns produtos de exemplo
lista_produtos = ListaProdutos()
lista_produtos.adicionar_produto("Pão", 3)
lista_produtos.adicionar_produto("Bolo", 4)
lista_produtos.adicionar_produto("Café", 2)

# Aplicando a promoção
lista_produtos.promocao()
