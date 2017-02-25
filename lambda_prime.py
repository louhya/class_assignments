def Opt_primes(n=int(input('Please enter a number: '))): # simple Sieve of Eratosthenes
    odds=list(range(3,n+1,2))
    sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds],[]))
    #print ([2] + [p for p in odds if p not in sieve])
    Plist = [2] + [p for p in odds if p not in sieve]
    for i in range(len(Plist)):
        print(Plist[i], 'is a prime number less than' , n)
Opt_primes()


