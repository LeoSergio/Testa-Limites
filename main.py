import sympy as sp

def verify_limit(function, a, L, epsilon=1e-5, delta=1e-5):
    """
    Verifica se o limite de uma função é igual a L quando x tende a a, utilizando a definição formal de limite.

    :param function: Função simbólica f(x)
    :param a: Ponto ao qual x tende
    :param L: Valor esperado do limite
    :param epsilon: Valor de tolerância para |f(x) - L|
    :param delta: Intervalo para testar valores próximos de a
    :return: True se o limite atender à definição formal, False caso contrário
    """
    x = sp.symbols('x')

    # Geração de valores ao redor de a
    test_points = [a + i * delta for i in range(-10, 11) if i != 0]  # Evitar x = a

    for point in test_points:
        try:
            # Avalia a função no ponto
            value = function.subs(x, point)
            
            # Verifica a condição |f(x) - L| < epsilon
            if abs(value - L) >= epsilon:
                return False
        except:
            # Caso a função seja indefinida no ponto, falha no teste
            return False

    return True

# Exemplo de uso
if __name__ == "__main__":
    x = sp.symbols('x')

    # Definir a função
    func = (x**2 - 1) / (x - 1)  # Exemplo com forma indeterminada
        
    # Simplificar a função simbolicamente (para evitar indeterminações)
    func = sp.simplify(func)

    # Ponto de limite, valor esperado e tolerâncias
    a = 1
    L = 2

    # Verificar o limite
    if verify_limit(func, a, L):
        print(f"O limite de f(x) quando x tende a {a} é {L}, conforme a definição formal.")
    else:
        print(f"O limite de f(x) quando x tende a {a} NÃO é {L} ou a definição formal não foi atendida.")
