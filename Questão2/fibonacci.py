def fibonacci(n, a=0, b=1):
    if n == a or n == b:
        return 1
    elif b > n:
        return 0
    return fibonacci(n, b, a + b)
def numeroDeFibonacci(num):
    if fibonacci(num):
        print(f'O número {num} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {num} não pertence à sequência de Fibonacci.')
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
numeroDeFibonacci(numero)