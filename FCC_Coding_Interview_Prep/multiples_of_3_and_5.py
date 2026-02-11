# sum of multiples of 3 and 5 for FCC practice. Pretty straightforward.

def multiples_of_3_and_5(number):
    total = 0
    for value in range(0, number):
        if value % 3 == 0 or value % 5 == 0:
            total += value
    return total

