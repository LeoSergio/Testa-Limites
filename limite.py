import sympy as sp

def verifica_limite(funcao, ponto_a, limite_L, epsilon):
    x = sp.symbols('x')  # Define x como variável simbólica
    
    # Simplifica a expressão para lidar com indeterminações
    funcao_simplificada = sp.simplify(funcao)
    
    # Calcula o limite da função simplificada
    limite_calculado = sp.limit(funcao_simplificada, x, ponto_a)
    
    # Verifica se o limite calculado é um número real
    if limite_calculado.is_real:
        # Verifica se o limite calculado está dentro do intervalo de epsilon do valor esperado
        if abs(limite_calculado - limite_L) < epsilon:
            return True, True  # Limite existe e é igual a L
        else:
            return False, True  # Limite existe, mas não é igual a L
    else:
        return False, False  # Limite não existe ou não é finito

def result():
    print("### Verificação de Limite usando Definição Formal ###")
    print("\nFormato de entrada da função f(x):")
    print(" - Use operadores matemáticos como: +, -, *, /, ** (potência), sqrt(x) (raiz quadrada).")
    print(" - Use funções trigonométricas como: sin(x) (seno), cos(x) (cosseno), tan(x) (tangente).")
    print(" - Exemplos de funções válidas:")
    print("   1. x**2 - 3*x + 1")
    print("   2. sqrt(x**2 + 1)")
    print("   3. 1/(x - 1)")
    print("   4. sin(x)/x")
    print("   5. cos(x) - 1")
    print("   6. tan(x)/x\n")

    try:
        # Solicita ao usuário os dados
        expressao = input("Digite a função f(x): ")
        ponto_a = float(input("Digite o ponto 'a' que x tende (ex: 0, 1, -1, π/2): "))
        epsilon = float(input("Digite o valor de epsilon (ex: 0.001): "))

        if epsilon <= 0:
            print("Erro: Epsilon deve ser um valor positivo.")
            return

        # Converte a expressão para uma função simbólica
        x = sp.symbols('x')
        funcao = sp.sympify(expressao)  # Converte string para expressão simbólica

        # Calcula o valor esperado do limite
        limite_L = sp.limit(funcao, x, ponto_a)

        # Calcula e testa o limite
        resultado, limite_existe = verifica_limite(funcao, ponto_a, limite_L, epsilon)

        # Exibição dos resultados
        print("\n### Exemplo Prático ###")
        print(f"Função f(x) = {funcao}")
        print(f"Função simplificada = {sp.simplify(funcao)}")
        print(f"Ponto de aproximação a = {ponto_a}")
        print(f"Valor esperado do limite L = {limite_L.evalf()}")
        print(f"Valor de epsilon = {epsilon}")

        if limite_existe:
            print("Resultado da verificação:", 
                  "O limite existe e é igual a L" if resultado else "O limite existe, mas não é igual a L")
        else:
            print("O limite não existe.")

        print("\n### Conclusão ###")
        if limite_existe:
            if resultado:
                print(f"O limite de f(x) quando x tende a {ponto_a} é {limite_L}, dentro da tolerância epsilon = {epsilon}.")
            else:
                print(f"O limite de f(x) existe, mas difere do valor esperado L = {limite_L}.")
        else:
            print(f"O limite de f(x) quando x tende a {ponto_a} não existe.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamada do programa principal
