# (a^b % c)
def exponenciacao_modular(a, b, c):
    if (b == 0):
        return 1

    temp = exponenciacao_modular(a, b / 2, c)
    if (b % 2):
        return (temp * temp * a) % c
    else:
        return (temp * temp) % c

print exponenciacao_modular(7, 57, 32)
