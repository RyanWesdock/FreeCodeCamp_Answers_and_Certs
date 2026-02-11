import math


def divisible_triangle_number(n):
    if not isinstance(n, int):
        print("number must be an integer")
        return 1
    if n <= 0:
        print("number must be a positive integer")
        return 2
    triangle_numbers = [0]
    divisors = []
    count = 1
    while len(divisors) < n:
        triangle_numbers.append(triangle_numbers[count - 1] + count)
        divisors = []
        x = int(math.sqrt(triangle_numbers[-1]) + 1)
        for j in range(1, x):
            if triangle_numbers[count] % j == 0:
                divisors.append(j)
        if len(divisors) >= (n/2):
            for k in range(x, triangle_numbers[-1] + 1):
                if triangle_numbers[count] % k == 0:
                    divisors.append(k)
        count += 1
    print(f'{triangle_numbers[count - 1]}: {divisors}')

    return 1


divisible_triangle_number(500)
