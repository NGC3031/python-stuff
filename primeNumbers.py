primes =[]
for n in range(2,100000):
    for x in range(2,n):
        if n % x ==0:
            #print(n, 'equals', x, '*', n//x)
            break
    else:
        primes.append(n)
        #print(n, " is a prime number")
print(primes)