# Find the largest prime factor of 22538679

def largest_prime_factor(num):
    lpf_list = []
    for i in range(1, num, 2):
        if num % i == 0:
            lpf_list.append(i)
    return lpf_list


print(largest_prime_factor(22538679))

# I gave the range function a step of 2 since we can rule out even numbers.
