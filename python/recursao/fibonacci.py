from datetime import datetime

def fibonacci(posicao):
    if posicao in (1, 2):
        return 1
    numero = fibonacci(posicao - 1) + fibonacci(posicao - 2) 
    return numero

def fibonacci_sem_fatorial(elemento):
    fibo = [0]
    fibo.append(1)
    fibo.append(1)
    for i in range (3, elemento + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    
    return fibo[elemento] 

print datetime.now()
print fibonacci(50)
print datetime.now()
print fibonacci_sem_fatorial(50)
print datetime.now()
