primes = [2, 3, 5, 7, 11]
primes[1] = 17
print(primes)

# primes[5] = 19

primes.append(13)
print(primes)

characters = []
characters.append("a")
print(len(characters))


primes.insert(1, 3)
print(primes)

n = primes.pop(2)
print(n)

primes.pop()
print(primes)

primes.remove(5)
print(primes)

