def is_prime(n):

    if n == 1:
        return False
    if n == 2:
        return True

    divisor = 2
    limit = int(n**0.5) + 1

    while  (divisor<limit) :

        if n%divisor == 0 :

            return False

        divisor += 1

    return True

        
        
