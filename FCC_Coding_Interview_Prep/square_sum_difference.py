def sum_square_difference(n):
    # error checking
    if not isinstance(n, int):
        print("value must be an integer")
        return 1
    if n <= 0:
        print("n must be a positive integer")
        return 2
    num_list = [x for x in range(0, n+1)]
    # sum of squares
    sum_of_squares = 0
    for value in num_list:
        sum_of_squares += value**2
    # square of sums
    sum_unsquared = 0
    square_of_sums = 0
    for value in num_list:
        sum_unsquared += value
    square_of_sums = sum_unsquared**2
    # find difference (square of sums is always larger)
    difference = square_of_sums - sum_of_squares
    print(f'The sum-square difference of the first {n} natural numbers is {difference}')
    return 1


sum_square_difference(100)
