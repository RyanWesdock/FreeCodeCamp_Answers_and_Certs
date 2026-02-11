def power_digit_sum(base, power):
    if not isinstance(base, int) or not isinstance(power, int):
        print("numbers must be integers")
        return 1
    if base <= 0 or power <= 0:
        print("numbers must be positive integers")
        return 2
    product = base**power
    print(product)
    digit_sum = 0
    for digit in str(product):
        digit_sum += int(digit)
    print(digit_sum)
    return 0


power_digit_sum(2, 75)
