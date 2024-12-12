def findPrimesA(number_of_primes):
    if number_of_primes == 0:
        return []
    primes = [2]
    if number_of_primes == 1:
        return primes
    current = 3
    x = 1
    while len(primes) < number_of_primes:
        prime = True
        if x*x < current:
                x += 1
        for i in primes:
            if current % i == 0:
                prime = False
                break
            if x < i:
                break
        if prime:
            primes.append(current)
            #print(current)
        current += 2
    return primes

if __name__ == "__main__":
    print(findPrimesA(1000000)[-1])