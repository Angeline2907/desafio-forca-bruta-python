import itertools
import time

def forca_bruta(caracteres, senha_secreta):
    print(f"Iniciando o ataque de força bruta...")
    print(f"Caracteres permitidos: '{caracteres}'")
    print(f"Senha alvo configurada: '{senha_secreta}'\n")
    
    # Testa comprimentos de senha de 1 até 3 caracteres
    for tamanho in range(1, 4):
        print(f"--- Testando combinações de tamanho {tamanho} ---")
        
        # Gera as combinações em formato de tupla
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            # Junta os caracteres em uma única string
            tentativa = "".join(combinacao)
            
            # Mostra o progresso das tentativas
            print(f"Tentando: {tentativa}")
            time.sleep(0.05)  # Pequena pausa para acompanhar no terminal
            
            # Verifica se encontrou a senha
            if tentativa == senha_secreta:
                print(f"\n🎉 Sucesso! A senha foi encontrada: '{tentativa}'")
                return True
                
    print("\n❌ Fim das tentativas. Senha não encontrada com até 3 caracteres.")
    return False

if __name__ == "__main__":
    # Configurações do desafio (pode alterar para testar)
    conjunto_caracteres = "abc"
    senha_alvo = "cab"
    
    forca_bruta(conjunto_caracteres, senha_alvo)
