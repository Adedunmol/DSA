

def isPrime(n):

    if n <= 1:
        return False
    
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    current = 5

    while current * current <= n:
        
        if n % current == 0 or n % (current + 2) == 0:
            return False

        current += 6

    return True


print(isPrime(2431))