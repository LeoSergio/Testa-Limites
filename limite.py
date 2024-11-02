import sympy as sp

def verifica_limite(funcao, ponto_a, limite_L, epsilon):
    x = sp.symbols('x')  # Define x como variável simbólica
    
    # Simplifica a expressão para lidar com indeterminações
    funcao_simplificada = sp.simplify(funcao)
    
    # Calcula o limite da função simplificada para ver se a indeterminação é resolvida
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

# Etapa de Entrada de Dados e Execução
def result():
    print("### Verificação de Limite usando Definição Formal ###")
    print("Formato de entrada da função f(x):")
    print(" - Use operadores como +, -, *, /, ** (para potenciação), e sqrt(x) para raiz quadrada.")
    print(" - Exemplos de funções:")
    print("   1. x**2 - 3*x + 1")
    print("   2. sqrt(x**2 + 1)")
    print("   3. 1/(x - 1)")
    print("   4. x**3 - 4*x + 4")

    # Solicita ao usuário os dados
    expressao = input("Digite a função f(x): ")
    ponto_a = float(input("Digite o ponto a que x tende: "))
    epsilon = float(input("Digite o valor de epsilon (ex: 0.001): "))

    # Converte a expressão para uma função simbólica
    x = sp.symbols('x')
    funcao = sp.sympify(expressao)  # Converte a entrada de string para expressão simbólica

    # Calcula o valor esperado do limite substituindo o ponto_a na função
    limite_L = sp.limit(funcao, x, ponto_a)

    # Calcula e testa o limite
    resultado, limite_existe = verifica_limite(funcao, ponto_a, limite_L, epsilon)

    # Exemplo Prático
    print("\n### Exemplo Prático ###")
    print(f"Função f(x) = {funcao}")
    print(f"Função simplificada = {sp.simplify(funcao)}")
    print(f"Ponto de aproximação a = {ponto_a}")
    print(f"Valor esperado do limite L = {limite_L}")
    print(f"Valor de epsilon = {epsilon}")
    if limite_existe:
        print("Resultado da verificação:", "O limite existe e é igual a L" if resultado else "O limite existe, mas não é igual a L")
    else:
        print("O limite não existe.")

    # Conclusão
    print("\n### Conclusão ###")
    if limite_existe:
        if resultado:
            print(f"O limite de f(x) quando x tende a {ponto_a} é igual a {limite_L}, de acordo com a definição formal e com o valor de epsilon = {epsilon}.")
        else:
            print(f"O limite de f(x) quando x tende a {ponto_a} existe, mas não é igual ao valor esperado de L = {limite_L}.")
    else:
        print(f"O limite de f(x) quando x tende a {ponto_a} não existe de acordo com a definição formal.")

    print("\nEste código verifica a existência e a igualdade do limite, permitindo checar se a função se aproxima corretamente de L conforme x se aproxima de a.")

# Chamada do programa principal

