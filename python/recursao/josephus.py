def josephus(n):
    if n == 1:
        return 1

    if (n % 2):
        return 2 * josephus(n / 2) + 1
    else:
        return 2 * josephus(n / 2) - 1

print josephus(10)
print josephus(5)
print josephus(123456)
