def largest_palindrome_product(n):
    if not isinstance(n, int):
        print("n must be an integer")
        return 1
    if n <= 1:
        print("n must be at least 2.")
        return 2
    integer_list = [x for x in range(10**(n-1), 10**n)]
    integer_list_copy = [x for x in integer_list]
    palindrome_product = 0
    palindrome_count = 0
    for value in integer_list:
        for value2 in integer_list_copy:
            contender = str(value * value2)
            if contender == contender[::-1] and int(contender) > palindrome_product:
                palindrome_product = int(contender)
                print(f'{value} X {value2} = {palindrome_product}')
                palindrome_count += 1
        integer_list_copy.remove(value)
    print(f'The largest palindrome product for {n} digits is {palindrome_product}.\n'
          f'For {n} digits, there are {palindrome_count} palindromes.')
    return 0


largest_palindrome_product(5)
