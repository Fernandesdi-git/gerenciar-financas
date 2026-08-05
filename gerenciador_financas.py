transacoes = []
def adicionar_transacao(tipo, valor, descricao):
    transacao = {"tipo": tipo, "valor": valor, "descricao": descricao}
    transacoes.append(transacao)

def calcular_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "Entrada":
            saldo = saldo + transacao["valor"]
        elif transacao ["tipo"] == "Saída":
            saldo = saldo - transacao["valor"]
    return saldo

def listar_transacoes():
    for transacao in transacoes:
        print(f"{transacao['tipo']} - R$ {transacao['valor']} - {transacao['descricao']}")
while True:
    print("1 - Adicionar transação")
    print("2 - Listar transações")
    print("3 - Ver saldo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        tipo = input("Digite o tipo (Entrada/Saída):")
        valor = float(input("Digite o valor:"))
        descricao = input("Digite a descrição:")
        adicionar_transacao(tipo, valor, descricao)
        print("Transacão Adicionada!")
    elif opcao == "2":
        listar_transacoes()
    elif opcao == "3":
        saldo = calcular_saldo()
        print(f"Saldo Atual: R$ {saldo}")
    elif opcao == "4":
        print("Encerrando o programa")
        break
