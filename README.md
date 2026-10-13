# Gerenciador de Finanças

Programa em Python com menu interativo para controle de finanças pessoais: registro de entradas e saídas, cálculo automático de saldo, listagem de transações e salvamento dos dados em arquivo.

## Sobre o projeto

Este projeto foi desenvolvido durante minha transição de carreira para tecnologia, e passou por uma evolução real ao longo do processo:

- **Versão 1**: estrutura de dados baseada em dicionários
- **Versão 2**: refatorado para Programação Orientada a Objetos (POO), incluindo classes, métodos e herança
- **Versão 3 (atual)**: adicionada persistência de dados em arquivo JSON, para que as transações não se percam ao fechar o programa

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
- Persistência de dados com arquivos JSON (`json.dump` / `json.load`)
- Reconstrução de objetos a partir de dicionários (distinguindo transações simples e recorrentes)
- Tratamento de exceções (`try/except`)
- Controle de versão com Git e uso de `.gitignore`

## Funcionalidades

- Adicionar uma transação simples (entrada ou saída)
- Adicionar uma transação recorrente (com frequência definida)
- Escolha do tipo da transação por número (1 - Entrada, 2 - Saída), evitando erros de digitação
- Listar todas as transações registradas
- Calcular e exibir o saldo atual
- Salvar as transações automaticamente em `transacoes.json` ao sair e carregá-las ao iniciar
- Menu interativo em loop até o usuário optar por sair

## Como executar

1. Tenha o Python instalado
2. Execute o arquivo `gerenciador_financas.py`
3. Siga as opções do menu exibido no terminal
4. Use a opção 5 para sair: é nela que os dados são salvos. O arquivo `transacoes.json` é criado automaticamente na primeira vez

## Próximos passos

Este projeto está em evolução contínua. Alguns próximos passos planejados:

- Adicionar categorias de gastos
- Adicionar validação de entradas (valores negativos, descrições vazias)
- Adicionar opção de remover ou editar transações
- Migrar a lógica para Java como parte da minha trilha de estudos
- Futuramente, transformar em uma API para consumo externo