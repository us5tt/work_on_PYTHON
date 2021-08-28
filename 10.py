def eratosthen(n):
    sieve = list(range(n))
    sieve[1] = 0
    for i in sieve[2:]:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

print(sum(eratosthen(2000000)))


def prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
            break
        return True

sum = 2
for n in range(3,2000000,2):
    if prime(n):
        sum += n
print(sum)