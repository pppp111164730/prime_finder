import time
import math

#old implementaion
def findPrime():
    arr = [2]
    current = 3
    while len(arr) < 10000:
        for i in arr:
            if current % i == 0:
                current += 1
                break
            if i == arr[-1]:
                arr.append(current)
    print(arr)
#findPrime()

#new implementation 
#at least twice as fast // this was wrong
def findPrime2_0():
    arr = [2]
    current = 3
    while len(arr) < 10000:
        for i in range(len(arr)):
            if current % arr[i] == 0:
                current += 2
                break
            if i == len(arr)-1:
                arr.append(current)
    print(arr, len(arr))
#findPrime2_0()

#I don't know how len() works but if it is an O(n) operstion then i think this would be better
#just looked it up len() is O(1) as it checks a list head element that is the length of the array

def findPrime2_1():
    arr = [2]
    current = 3
    ArrayLength = 1
    while ArrayLength < 10000:
        for i in range(len(arr)):
            if current % arr[i] == 0:
                current += 2
                break
            if i == len(arr)-1:
                arr.append(current)
                ArrayLength += 1
    #print(arr, len(arr))
def findPrime2_1():
    arr = [2]
    current = 3
    ArrayLength = 1
    while ArrayLength < 10000:
        for i in range(len(arr)):
            if current % arr[i] == 0:
                current += 2
                break
            if i == len(arr)-1:
                arr.append(current)
                ArrayLength += 1

def findPrimes(number_of_primes):#tester
    if number_of_primes == 0:
        return []
    primes = [2]
    if number_of_primes == 1:
        return primes
    current = 3
    while len(primes) < number_of_primes:
        prime = True
        for i in primes:
            if current % i == 0:
                prime = False
                break
        if prime:
            primes.append(current)
            #print(current)
        current += 2
    return primes

def findPrimesA(number_of_primes):#new best and the big O lost and n and gained a square root of n multiplier.
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

def findPrimesP(number_of_primes):#add prealocation in this way was not good doubled the time
    if number_of_primes == 0:
        return []
    primes = [0] * number_of_primes
    primes[0] = 2
    primes_current = 1
    if number_of_primes == 1:
        return primes
    current = 3
    x = 1
    while primes[number_of_primes - 1] == 0:# len(primes) < number_of_primes:
        prime = True
        if x*x < current:
                x += 1
        for i in primes[:primes_current]:
            if x < i:
                break
            if current % i == 0:
                prime = False
                break
        if prime:
            primes[primes_current] = current
            primes_current += 1
            #print(current)
        current += 2
    return primes

def findPrimesb(number_of_primes):#old best.
    if number_of_primes == 0:
        return []
    primes = [2]
    if number_of_primes == 1:
        return primes
    current = 3
    while len(primes) < number_of_primes:
        prime = True
        for i in primes:
            if current % i == 0:
                prime = False
                break
            if math.sqrt(current) < i:
                break
        if prime:
            primes.append(current)
            #print(current)
        current += 2
    return primes

def findPrimesB(number_of_primes):
    if number_of_primes == 0:
        return []
    primes = [2]
    if number_of_primes == 1:
        return primes
    current = 3
    half = 0
    while len(primes) < number_of_primes:
        prime = True
        if primes[half] < (current >> 1) + 1:
            half += 1
        for i in range(half):
            if current % primes[i] == 0:
                prime = False
                break
        if prime:
            primes.append(current)
            #print(current)
        current += 2
    return primes

def findNoMod(num):#slower than findPrimes
    if num < 1:
        return []
    if num == 1:
        return [2]
    primes = [2]
    prime_multiples = [2]
    current = 3
    while len(primes) < num:
        prime = True
        for i in range(len(primes)):
            while prime_multiples[i] < current:
                prime_multiples[i] += primes[i]
        for i in range(len(primes)):
            if current == prime_multiples[i]:
                prime = False
                break
        if prime:
            primes.append(current)
            prime_multiples.append(current)
        current += 2
    return primes

def findNoMod2(num):#slower than findPrimes but faster than findNoMod
    if num < 1:
        return []
    if num == 1:
        return [2]
    primes = [2]
    prime_multiples = [2]
    current = 3
    while len(primes) < num:
        prime = True
        for i in range(len(primes)):
            if prime_multiples[i] < current:
                prime_multiples[i] += primes[i] 
        for i in range(len(primes)):
            if current == prime_multiples[i]:
                prime = False
                break  
        if prime:
            primes.append(current)
            prime_multiples.append(current)
        current += 2
    return primes

def findNoMod3(num):#slower than findPrimes but faster than findNoMod2
    if num < 1:
        return []
    if num == 1:
        return [2]
    primes = [2]
    prime_multiples = [2]
    current = 3
    half = 0
    while len(primes) < num:
        prime = True
        if primes[half] < (current // 2) +1:
            half += 1
        for i in range(half):
            if prime_multiples[i] < current:
                prime_multiples[i] += primes[i] 
        for i in range(len(primes)):
            if current == prime_multiples[i]:
                prime = False
                break  
        if prime:
            primes.append(current)
            prime_multiples.append(current)
        current += 2
    return primes

if __name__ == "__main__":

    start_time = time.time()

    print("start")
    #findPrime2_1()
    print(findPrimesP(10))
    #if findPrimesA(10000) == findPrimesP(10000):
    #    print(True)
    #if findPrimes(30000) == findPrimesb(30000):
    #    print(True)
    #findNoMod(10000)
    print(findPrimesP(10000)[5])
    #print(findNoMod(10))
    #print(findPrimes(10))
    print('done')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    #------------------------------------------------
    start_time = time.time()

    print("start")
    #findPrime2_1()
    #findPrimes(30000)# estimate of 6 seconds run time
    findPrimesA(100000)
    #findNoMod2(10000)
    print('done')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
    #-------------------------------------------------
    start_time = time.time()
    #print(findPrimes(100000)[-1])
    #findNoMod3(10000)#estimate of 10 minutes run time
    findPrimesP(100000)
    print('finished')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")



