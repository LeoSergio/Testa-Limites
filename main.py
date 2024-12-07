if __name__ == "__main__":
    import math

    # Função f(x) a ser testada
    f = lambda x: 2 * x + 3  # Exemplo de função linear

    # Parâmetros
    c = 2  # Ponto em que o limite está sendo avaliado
    L = 7  # Valor do limite esperado
    epsilon = 0.01
    delta = 0.01

    # Geração de valores de x manualmente
    x_valores = [c - delta + i * 0.0001 for i in range(int(2 * delta / 0.0001))]
    x_valores = [x for x in x_valores if x != c]  # Remove o ponto c

    # Verificação da definição formal
    limite_valido = True

    for x in x_valores:
        if not (0 < abs(x - c) < delta and abs(f(x) - L) < epsilon):
            limite_valido = False
            break

    # Resultado
    print(f"Para ε = {epsilon} e δ = {delta}, a definição é : {'satisfeita' if limite_valido else 'não satisfeita'}.")
