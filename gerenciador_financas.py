import json
transacoes = [] 

class Transacao:
    def __init__(self, tipo, valor, descricao):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao

    def exibir(self):
        print(f"{self.tipo} - R$ {self.valor} - {self.descricao}")
    def eh_valor_alto(self):
        if self.valor > 1000:
            return True
        else:
            return False
    def aplicar_taxa(self, percentual):
        self.valor = self.valor - (self.valor * percentual / 100)

def adicionar_transacao(transacao):
    transacoes.append(transacao)
def calcular_saldo():
    saldo = 0
    for t in transacoes:
        if t.tipo == "Entrada":
            saldo = saldo + t.valor
        elif t.tipo == "Saída":
            saldo = saldo - t.valor
    return saldo 
def salvar_transacoes():
    dados = []
    for t in transacoes:
        dados.append(t.__dict__)
    with open("transacoes.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_transacoes():
    try:
        with open("transacoes.json", "r") as arquivo:
            dados = json.load(arquivo)
            for d in dados:
                if "frequencia" in d:
                    t = TransacaoRecorrente(d["tipo"], d["valor"], d["descricao"], d["frequencia"])
                else:
                    t = Transacao(d["tipo"], d["valor"], d["descricao"])
                transacoes.append(t)
    except FileNotFoundError:
        pass

class TransacaoRecorrente(Transacao):
    def __init__ (self, tipo, valor, descricao, frequencia):
        super().__init__(tipo, valor, descricao)
        self.frequencia = frequencia

carregar_transacoes()

for t in transacoes:
    t.exibir()
saldo = calcular_saldo()
while True:
    print("\n1 - Adicionar transação")
    print("2 - Adicionar transação recorrente")
    print("3 - Listar transações")
    print("4 - Ver saldo")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        escolha = input("Tipo (1 - Entrada, 2 -Saída): ")
        if escolha == "1":
            tipo = "Entrada"
        elif escolha == "2":
            tipo = "Saída"
        else:
            print("Opção inválida.")
            continue
        valor = float(input("Valor: "))
        descricao = input("Descrição: ")
        nova = Transacao(tipo, valor, descricao)
        adicionar_transacao(nova)
    elif opcao == "2":
        escolha = input("Tipo (1 - Entrada, 2 -Saída): ")
        if escolha == "1":
            tipo = "Entrada"
        elif escolha == "2":
            tipo = "Saída"
        else:
            print("Opção inválida.")
            continue
        valor = float(input("Valor: "))
        descricao = input("Descrição: ")
        frequencia = input("Frequência: ")
        nova = TransacaoRecorrente(tipo, valor, descricao, frequencia)
        adicionar_transacao(nova)
    elif opcao == "3":
        for t in transacoes:
            t.exibir()
    elif opcao == "4":
        saldo = calcular_saldo()
        print(f"Saldo: R$ {saldo}")
    elif opcao == "5":
        salvar_transacoes()
        break
