def prime_factors_finder(n):
    factors = []
    factor = 2
    
    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            factor += 1

    return factors

number = int(input("Enter a number: "))
result = prime_factors_finder(number)
print(f"The prime factors of {number}: {result}")
