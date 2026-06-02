# Compiladores

Este repositório contém um gerenciador de tabela de símbolos em Python.

## Requisitos

- Python 3.11 ou superior instalado
- O comando `python` deve estar disponível no PATH do Windows

## Como executar

1. Abra o PowerShell ou outro terminal.
2. Navegue até a pasta do projeto:

```powershell
cd C:\Users\ACEQUIP\Compiladores
```

3. Execute o script:

```powershell
python .\tabelaSimbolos.py
```

4. Use as opções do menu para interagir:

- `1` ou `declarar` para declarar uma variável
- `2` ou `buscar` para buscar uma variável
- `3` ou `entrar` para abrir um novo escopo
- `4` ou `sair` para fechar o escopo atual
- `5` ou `print` para exibir a pilha de escopos
- `6` ou `exit` para encerrar o programa

## Exemplo rápido

```powershell
python .\tabelaSimbolos.py
```

Digite `1` e informe `nome tipo`, por exemplo:

```text
Digite o comando ou o número da opção: 1
Digite nome e tipo da variável separados por espaço: x int
```

Digite `2` para buscar:

```text
Digite o comando ou o número da opção: 2
Digite o nome da variável para buscar: x
```
