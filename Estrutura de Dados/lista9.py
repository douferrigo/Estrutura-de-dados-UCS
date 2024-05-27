def funcao_hash(chave, tamanho_tabela):
    valor = 5381
    for caractere in chave:
        valor = 33 * valor + ord(caractere)
        valor = valor % tamanho_tabela
        return valor

print(funcao_hash("João", 1024))
print(funcao_hash("Maria", 1024))