class Produto:
    def __init__(self,codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo
    def __repr__(self):
        return '%s->%s' % (self.codigo, self.proximo)
class ListaEncadeada:
    def __init__(self):
        self.cabeca= None
    def __repr__(self):
        return "["+ str(self.cabeca) + "]"
def AddFinal(self, novoCod):
    if self.cabeca is None:  # Se a lista estiver vazia
        self.cabeca = Produto(novoCod)
    else:
        atual = self.cabeca
        while atual.proximo is not None:  # Encontra o último nó
            atual = atual.proximo    
        atual.proximo = Produto(novoCod)
    
#Testes
lista = ListaEncadeada()
print("Lista vazia:", lista)
AddFinal(lista, 1111)
print(lista)
AddFinal (lista, 2222)
print(lista)
AddFinal (lista, 3333112121)
print (lista)    