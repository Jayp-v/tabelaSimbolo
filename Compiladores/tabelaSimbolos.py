import sys

class GerenciadorTabelaSimbolos:
    def __init__(self):
        self.pilha_escopos = [{}]

    def entrar_escopo(self):
        """Abre um novo escopo aninhado (ex: ao entrar em uma função ou bloco if/for)"""
        self.pilha_escopos.append({})
        print("[INFO] Novo escopo aberto.")

    def sair_escopo(self):
        """Fecha o escopo atual, descartando suas variáveis localmente"""
        if len(self.pilha_escopos) > 1:
            self.pilha_escopos.pop()
            print("[INFO] Escopo atual fechado (variáveis locais descartadas).")
        else:
            print("[ERRO] Não é possível fechar o escopo global.")

    def declarar(self, variavel, tipo):
        """Insere uma nova variável no escopo que está no topo da pilha"""
        escopo_atual = self.pilha_escopos[-1]
        if variavel in escopo_atual:
            print(f"[ERRO SEMÂNTICO] Variável '{variavel}' já declarada neste escopo.")
            return False
        else:
            escopo_atual[variavel] = tipo
            print(f"[SUCESSO] Declarado: '{variavel}' do tipo '{tipo}' no escopo atual.")
            return True

    def buscar(self, variavel):
        """Busca a variável do topo da pilha até a base (escopos mais externos)"""
        for escopo in reversed(self.pilha_escopos):
            if variavel in escopo:
                return escopo[variavel]
        return None

    def exibir_pilha(self):
        """Função auxiliar para debugar e visualizar o estado atual da pilha"""
        print("\n--- ESTADO ATUAL DA PILHA DE ESCOPOS ---")
        for i, escopo in enumerate(reversed(self.pilha_escopos)):
            nivel = len(self.pilha_escopos) - 1 - i
            nome_escopo = "Global" if nivel == 0 else f"Local (Nível {nivel})"
            print(f"{nome_escopo}: {escopo}")
        print("----------------------------------------\n")


def exibir_menu():
    print("\n=== GERENCIADOR DE TABELA DE SÍMBOLOS ===")
    print("1. Declarar variável (declarar id tipo)")
    print("2. Buscar variável (buscar id)")
    print("3. Entrar em novo escopo (entrar)")
    print("4. Sair do escopo atual (sair)")
    print("5. Exibir pilha de escopos")
    print("6. Sair do programa")

def main():
    gerenciador = GerenciadorTabelaSimbolos()
    
    while True:
        exibir_menu()
        comando = input("\nDigite o comando ou o número da opção: ").strip().split()
        
        if not comando:
            continue
            
        opcao = comando[0].lower()
        
        if opcao == '1' or opcao == 'declarar':
            if len(comando) < 3:
                extra = input("Digite nome e tipo da variável separados por espaço: ").strip().split()
                if len(extra) < 2:
                    print("[ERRO] Uso correto: declarar <nome_da_variavel> <tipo>")
                else:
                    gerenciador.declarar(extra[0], extra[1])
            else:
                gerenciador.declarar(comando[1], comando[2])
                
        elif opcao == '2' or opcao == 'buscar':
            if len(comando) < 2:
                nome = input("Digite o nome da variável para buscar: ").strip()
                if not nome:
                    print("[ERRO] Uso correto: buscar <nome_da_variavel>")
                else:
                    tipo = gerenciador.buscar(nome)
                    if tipo:
                        print(f"[SUCESSO] Variável '{nome}' encontrada! Tipo: '{tipo}'")
                    else:
                        print(f"[ERRO SEMÂNTICO] Variável '{nome}' não foi declarada em nenhum escopo visível.")
            else:
                tipo = gerenciador.buscar(comando[1])
                if tipo:
                    print(f"[SUCESSO] Variável '{comando[1]}' encontrada! Tipo: '{tipo}'")
                else:
                    print(f"[ERRO SEMÂNTICO] Variável '{comando[1]}' não foi declarada em nenhum escopo visível.")
                    
        elif opcao == '3' or opcao == 'entrar':
            gerenciador.entrar_escopo()
            
        elif opcao == '4' or opcao == 'sair':
            gerenciador.sair_escopo()
            
        elif opcao == '5' or opcao == 'print':
            gerenciador.exibir_pilha()
            
        elif opcao == '6' or opcao == 'exit':
            print("Encerrando o simulador.")
            sys.exit(0)
        else:
            print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    main()