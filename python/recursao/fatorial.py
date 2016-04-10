
def fatorial(numero):
    if numero == 0:
        return 1

    return numero * fatorial(numero - 1)

def fatorial_sem_recursao(numero):
    if numero == 0:
        return 1

    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

print fatorial(5)
print fatorial_sem_recursao(5)
