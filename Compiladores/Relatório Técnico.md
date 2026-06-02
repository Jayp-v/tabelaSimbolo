# Relatório Técnico

## Introdução

Este relatório descreve a implementação do gerenciador de tabela de símbolos desenvolvido em Python. O objetivo é fornecer uma ferramenta simples para declarar, buscar e gerenciar variáveis em escopos aninhados, suportando operações básicas de análise semântica.

## Metodologia de Implementação

O código foi organizado em uma classe principal, `GerenciadorTabelaSimbolos`, que mantém uma pilha de dicionários representando escopos aninhados. Cada escopo é adicionado ao entrar em um novo bloco e removido ao sair.

As operações principais são:

- `entrar_escopo()`: adiciona um novo escopo vazio à pilha.
- `sair_escopo()`: remove o escopo atual, exceto o escopo global.
- `declarar(variavel, tipo)`: insere uma variável no escopo atual e valida declarações duplicadas.
- `buscar(variavel)`: procura a variável do escopo atual até o global, retornando o tipo se encontrada.
- `exibir_pilha()`: mostra o estado atual da pilha de escopos para facilitar a depuração.

A interface interativa em `main()` apresenta um menu de opções, recebendo comandos e solicitando informações adicionais quando necessário.

## Casos de Teste

1. Declaração de variável no escopo global
   - Passos:
     1. Executar o programa.
     2. Digitar `1` e pressionar Enter.
     3. Digitar `x int` e pressionar Enter.
   - Saída esperada:
     - `Digite o comando ou o número da opção: 1`
     - `Digite nome e tipo da variável separados por espaço: x int`
     - `[SUCESSO] Declarado: 'x' do tipo 'int' no escopo atual.`
   - Critério de sucesso: a variável `x` passa a existir no escopo global.

2. Busca de variável declarada
   - Passos:
     1. Após declarar `x int`, digitar `2` e pressionar Enter.
     2. Digitar `x` e pressionar Enter.
   - Saída esperada:
     - `Digite o comando ou o número da opção: 2`
     - `Digite o nome da variável para buscar: x`
     - `[SUCESSO] Variável 'x' encontrada! Tipo: 'int'`
   - Critério de sucesso: a busca retorna o tipo correto para `x`.

3. Declaração duplicada no mesmo escopo
   - Passos:
     1. Declarar `x int` no escopo global.
     2. Tentar declarar `x int` novamente no mesmo escopo.
   - Saída esperada:
     - `[ERRO SEMÂNTICO] Variável 'x' já declarada neste escopo.`
   - Critério de sucesso: o segundo registro não deve ser aceito e deve manter o valor anterior.

4. Escopo aninhado e visibilidade de variáveis
   - Passos:
     1. Declarar `x int` no escopo global.
     2. Digitar `3` para entrar em novo escopo.
     3. Declarar `y float` neste escopo interno.
     4. Buscar `y` e confirmar existência.
     5. Digitar `4` para sair do escopo interno.
     6. Buscar `y` novamente.
   - Saída esperada:
     - Ao buscar `y` dentro do escopo interno: `[SUCESSO] Variável 'y' encontrada! Tipo: 'float'`
     - Após sair do escopo: `[ERRO SEMÂNTICO] Variável 'y' não foi declarada em nenhum escopo visível.`
   - Critério de sucesso: variáveis internas ficam visíveis apenas dentro do escopo onde foram declaradas.

5. Exibição da pilha de escopos
   - Passos:
     1. Declarar `a int` no escopo global.
     2. Entrar em novo escopo.
     3. Declarar `b bool` no escopo interno.
     4. Digitar `5` para exibir a pilha.
   - Saída esperada:
     - Impressão de ambos os escopos, por exemplo:
       - `Global: {'a': 'int'}`
       - `Local (Nível 1): {'b': 'bool'}`
   - Critério de sucesso: a estrutura de escopos deve corresponder ao estado atual do programa.

6. Tentar sair do escopo global
   - Passos:
     1. Garantir que o programa esteja no escopo global.
     2. Digitar `4` e pressionar Enter.
   - Saída esperada:
     - `[ERRO] Não é possível fechar o escopo global.`
   - Critério de sucesso: o programa não remove o escopo global e mantém as variáveis existentes.

7. Caso de teste de fluxo completo
   - Passos:
     1. Declarar `x int` no global.
     2. Entrar em novo escopo.
     3. Declarar `x float` no escopo interno.
     4. Buscar `x` e confirmar que retorna `float`.
     5. Sair do escopo interno.
     6. Buscar `x` novamente e confirmar que retorna `int`.
   - Saída esperada:
     - Busca interna: `[SUCESSO] Variável 'x' encontrada! Tipo: 'float'`
     - Busca após sair: `[SUCESSO] Variável 'x' encontrada! Tipo: 'int'`
   - Critério de sucesso: a resolução de nomes deve respeitar a visibilidade e esconder variáveis de escopos externos quando apropriado.
