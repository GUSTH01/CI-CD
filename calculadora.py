
def soma(a, b):
    return a - b  # Erro proposital

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
