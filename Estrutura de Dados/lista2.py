class Produto:
    def __init__(self, Codigo="Indefinido", Peso=0):
        self.Codigo = Codigo
        self.Tipo = Peso

    def __repr__(self):
        return '%s -> %d' % (self.Codigo, self.Tipo)

class Nodo:
    def __init__(self, dado=None, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.conteudo, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def __repr__(self):
        return "[" + str(self.inicio) + "]"

    def ListaVazia(self):
        return self.inicio is None

    def ImprimeLista(self):
        atual = self.inicio
        cont = 0
        print("Inicio da lista")
        if self.ListaVazia():
            print("A lista está vazia")
        else:
            while atual is not None:
                print("Posição:", cont, atual)
                cont += 1
                atual = atual.proximo
        print("Final da lista")

    def TotalProdutosRefrigerados(self):
        total = 0
        atual = self.inicio
        while atual is not None:
            if atual.conteudo.Tipo == 1:  # Ajuste para acessar o atributo Tipo do objeto Produto
                total += 1
                atual = atual.proximo
        return total

    def NovoProduto(self, produto):
        novo_no = Nodo(produto)  # Criando um novo nó com o produto
        if self.inicio is None:  # Se a lista estiver vazia, o novo nó será o início
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:  # Percorrendo a lista até o último nó
                atual = atual.proximo
            atual.proximo = novo_no  # Adicionando o novo nó no final da lista

    def CompararListas(self, outra_lista):
        lista1 = self.inicio
        repete = ListaEncadeada()
        while lista1 is not None:
            lista2 = outra_lista.inicio
            while lista2 is not None:
                if lista1.conteudo.Codigo == lista2.conteudo.Codigo:
                    repete.NovoProduto(lista1.conteudo)
                    break
                lista2 = lista2.proximo
            lista1 = lista1.proximo
        return repete

# Exemplo de uso
lista = ListaEncadeada()
lista2 = ListaEncadeada()

lista.NovoProduto(Produto("001", 1))
lista.NovoProduto(Produto("002", 0))
lista.NovoProduto(Produto("003", 1))
lista.NovoProduto(Produto("004", 1))
lista.NovoProduto(Produto("005", 0))
lista.NovoProduto(Produto("006", 0))
lista2.NovoProduto(Produto("001", 1))
lista2.NovoProduto(Produto("002", 0))
lista2.NovoProduto(Produto("003", 1))
lista2.NovoProduto(Produto("009", 1))
lista2.NovoProduto(Produto("008", 0))
lista2.NovoProduto(Produto("007", 0))

repetidos = lista.CompararListas(lista2)
print("Produtos repetidos:", lista.CompararListas(lista2))
repetidos.ImprimeLista()