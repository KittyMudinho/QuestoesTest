def fibonacci(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    return fibonacci(n-1)+fibonacci(n-2)
def eFib(n):
    j=0
    while True:
        val=fibonacci(j)
        j+=1
        if(n==val):
            print(f'O número {n} está na sequência de Fibonacci.')
            break
        elif (val>n):
            print(f'O número {n} não está na sequência de Fibonacci.')
            break
n=int(input('Escreva um número para saber se ele faz parte da sequência de Fibonacci: '))
eFib(n)
