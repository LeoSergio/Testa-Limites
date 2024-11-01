import sympy as sp

def verifica_limite(funcao, ponto_a, limite_L, epsilon):
    x = sp.symbols('x')  # Define x como variável simbólica
    f = sp.lambdify(x, funcao)  # Converte a função simbólica para uma função Python

    delta = 0.1
    limite_existe = True  # Assume inicialmente que o limite existe

    while delta > 1e-6:  # Reduz delta para uma verificação mais precisa
        x_esquerda = ponto_a - delta
        x_direita = ponto_a + delta

        try:
            # Calcula |f(x) - L| para valores à esquerda e à direita de ponto_a
            fx_esquerda = abs(f(x_esquerda) - limite_L)
            fx_direita = abs(f(x_direita) - limite_L)
        except ZeroDivisionError:
            return False, False  # Divisão por zero indica descontinuidade, limite não existe

        print(f"Testando com delta = {delta}: |f({x_esquerda}) - L| = {fx_esquerda}, |f({x_direita}) - L| = {fx_direita}")
        
        # Verifica a condição de limite |f(x) - L| < epsilon
        if fx_esquerda >= epsilon or fx_direita >= epsilon:
            return False, True  # Limite existe mas não é igual a L

        delta /= 2  # Reduz delta para maior precisão

    return True, True  # O limite existe e é igual a L

# Etapa de Entrada de Dados
print("### Verificação de Limite usando Definição Formal ###")
print("Formato de entrada da função f(x):")
print(" - Use operadores como +, -, *, /, ** (para potenciação), e sqrt(x) para raiz quadrada.")
print(" - Exemplos de funções:")
print("   1. x**2 - 3*x + 1")
print("   2. sqrt(x**2 + 1)")
print("   3. 1/(x - 1)")
print("   4. x**3 - 4*x + 4")

expressao = input("Digite a função f(x): ")
ponto_a = float(input("Digite o ponto a que x tende: "))
epsilon = float(input("Digite o valor de epsilon (ex: 0.001): "))

# Converte a expressão para uma função simbólica
x = sp.symbols('x')
funcao = sp.sympify(expressao)  # Converte a entrada de string para expressão simbólica

# Definindo o valor esperado do limite de acordo com a função e o ponto
limite_L = funcao.subs(x, ponto_a)  # Calcula o limite esperado substituindo ponto_a na função

# Calcula e testa o limite
resultado, limite_existe = verifica_limite(funcao, ponto_a, limite_L, epsilon)

# Exemplo Prático
print("\n### Exemplo Prático ###")
print(f"Função f(x) = {funcao}")
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

