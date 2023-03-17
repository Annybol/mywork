# Generate primes
#Author: Anne Boland

primes = []
upto = 100001
for candidate in range(2, upto):
    #print (candidate)
    isPrime = True
    for divisor in range(2,candidate):
        #line 9 can also be for divisor in primes
        if (candidate % divisor ==0):
            isPrime = False
            # we dont need to keep checking if false 
            break
    primes.append(candidate)

print(primes)