def special_pythagorean_triplet(n):
    if not isinstance(n, int):
        print("number must be an integer")
        return 1
    if n <= 0:
        print("number must be a positive integer")
        return 2
    for a in range(1, n + 1):
        for b in range(1, round((n / 2)) + 1):
            x = a**2 + b**2
            if x**(1/2) == int(x**(1/2)):
                c = int(x**(1/2))
                if (a + b + c) == n:
                    pythagorean_product = a * b * c
                    print(a, b, c)
                    print(pythagorean_product)
                    return 0


special_pythagorean_triplet(120)
