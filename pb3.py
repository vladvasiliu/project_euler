# https://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# recursive version
def factor(num):
    div = 1
    result = []
    
    while True:
        div += 1
        if div * div > num:
            return [num]
        
        q, r = divmod(num, div)

        if r != 0:
            continue

        result.extend(factor(q))
        result.extend(factor(div))
        return result
