#generator.py

def isprime(n):
	if n == 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	else:
		return True
pass

def primes(n = 1):
	while(True):
		if isprime(n): yield n
		n += 1
pass

for n in primes():
	if n > 100: break
	print(n)

