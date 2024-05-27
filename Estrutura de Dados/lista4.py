class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"{self.valor} de {self.naipe}"

class Monte:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def __repr__(self):
        if self.cartas:
            return f"Monte: {self.cartas[-1]}"
        else:
            return "Monte vazio"

def distribuir_cartas():
    baralho = []
    for valor in range(1, 14):
        for naipe in ["Ouros", "Copas", "Espadas", "Paus"]:
            baralho.append(Carta(valor, naipe))

    montes = [Monte() for _ in range(8)]  # Criar os oito montes

    # Distribuir as cartas nos montes de acordo com as regras do jogo
    for i in range(7):
        for j in range(i + 1):
            montes[i].adicionar_carta(baralho.pop(0))

    for monte in montes:
        print(monte)

# Distribuir as cartas nos montes
distribuir_cartas()
