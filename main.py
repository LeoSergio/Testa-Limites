import limite

def main():
    while True:
        print("\n=== Menu de Cálculos ===")
        print("1 - Limites")
        print("2 - Derivadas")
        print("3 - Integrais")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Você selecionou a opção para calcular Limites.")
            limite.result()
            # Aqui você pode chamar a função de cálculo de limites
        elif opcao == '2':
            print("Você selecionou a opção para calcular Derivadas.")
            # Aqui você pode chamar a função de cálculo de derivadas
        elif opcao == '3':
            print("Você selecionou a opção para calcular Integrais.")
            # Aqui você pode chamar a função de cálculo de integrais
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Chamando a função para exibir o menu
if __name__ == "__main__":
    main()