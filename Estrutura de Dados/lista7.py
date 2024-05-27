from collections import deque

def verifica_palindromo(entrada):
    fila = deque(entrada)
    while len(fila) > 1:
        if fila.popleft() != fila.pop():
            return "Não é palíndromo"  
        return "É palíndromo"
    
entrada_usuario = input("Digite uma sequência de caracteres: ")
resultado = verifica_palindromo(entrada_usuario)
print(resultado)