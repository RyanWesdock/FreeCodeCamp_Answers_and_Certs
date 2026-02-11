def nth_prime(n):
    if not isinstance(n, int):
        print("number must be an integer")
        return 1
    if n <= 0:
        print("number must be a positive integer")
        return 2
    nums = [2, 3, 4]
    primes = [2, 3]
    contender = 4
    while len(primes) < n:
        possible_prime = True
        contender += 1
        if contender % 2 != 0:
            for tester in nums:
                if contender % tester == 0:
                    possible_prime = False
                    break
            if possible_prime:
                primes.append(contender)
            nums.append(contender)
    final_prime = primes[len(primes) - 1]
    print(f'The {n} prime is {final_prime}')
    return True


nth_prime(10001)
