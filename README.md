# Gerenciador de Finanças

Programa em Python com menu interativo para controle de finanças pessoais: registro de entradas e saídas, cálculo automático de saldo e listagem de transações.

## Sobre o projeto

Este projeto foi desenvolvido durante minha transição de carreira para tecnologia, e passou por uma evolução real ao longo do processo:

- **Versão 1**: estrutura de dados baseada em dicionários
- **Versão 2 (atual)**: refatorado para Programação Orientada a Objetos (POO), incluindo classes, métodos e herança

## Conceitos aplicados

- Variáveis e tipos de dados (incluindo conversão com float)
- Estruturas condicionais (if/elif/else)
- Laços de repetição (for e while)
- Interação com o usuário (input)
- Programação Orientada a Objetos:
  - Classes e objetos
  - Construtor (`__init__`)
  - Atributos e métodos
  - Herança (`TransacaoRecorrente` herda de `Transacao`)

## Funcionalidades

- Adicionar uma transação simples (entrada ou saída)
- Adicionar uma transação recorrente (com frequência definida)
- Listar todas as transações registradas
- Calcular e exibir o saldo atual
- Menu interativo em loop até o usuário optar por sair

## Como executar

1. Tenha o Python instalado
2. Execute o arquivo `gerenciador_financas.py`
3. Siga as opções do menu exibido no terminal

## Próximos passos

Este projeto está em evolução contínua. Alguns próximos passos planejados:

- Adicionar categorias de gastos
- Salvar os dados em arquivo, para que não se percam ao encerrar o programa
- Adicionar opção de remover ou editar transações
- Migrar a lógica para Java como parte da minha trilha de estudos
- Futuramente, transformar em uma API para consumo externo
