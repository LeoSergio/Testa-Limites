import sympy as sp

def verifica_limite(funcao, ponto_a, limite_L, epsilon=0.001):
    x = sp.symbols('x')  # Define x como variável simbólica
    f = sp.lambdify(x, funcao)  # Converte a função simbólica para uma função Python

    # Inicializa o valor de delta, tentamos diferentes valores de delta
    delta = 0.1
    while delta > 1e-6:  # Reduz delta até certo limite para maior precisão
        # Teste valores à esquerda e à direita de 'a' para |x - a| < delta
        x_esquerda = ponto_a - delta / 2
        x_direita = ponto_a + delta / 2
        
        # Calcula |f(x) - L| para x_esquerda e x_direita
        fx_esquerda = abs(f(x_esquerda) - limite_L)
        fx_direita = abs(f(x_direita) - limite_L)
        
        # Verifica se |f(x) - L| < epsilon
        if fx_esquerda >= epsilon or fx_direita >= epsilon:
            return False  # Não atende à definição formal, o limite não é igual a L
        
        delta /= 2  # Reduz delta para uma verificação mais precisa

    return True  # Passou no teste, o limite parece ser igual a L

# Exemplo de uso
x = sp.symbols('x')
funcao = x**2  # Função de exemplo f(x) = x^2
ponto_a = 2    # Queremos o limite quando x -> 2
limite_L = 4   # Esperamos que o limite seja 4

resultado = verifica_limite(funcao, ponto_a, limite_L)
print("O limite é igual a L?" , resultado)
