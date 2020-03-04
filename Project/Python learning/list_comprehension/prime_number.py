def prime_number(max_range):
    non_primes = [ j for i in range(2,8) for j in range(i*2, max_range, i) ]
    prime = [ x for x in range(2, max_range) if x not in non_primes ]
    return print(prime)
prime_number(100)

