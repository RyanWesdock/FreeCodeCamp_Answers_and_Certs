def recursive_collatz(num, num_li):
    if num == 1:
        num_li.append(num)
        return
    elif num % 2 == 0:
        num_li.append(num)
        return recursive_collatz(num / 2, num_li)
    else:
        num_li.append(num)
        return recursive_collatz(3 * num + 1, num_li)


def longest_collatz_sequence(limit):
    if not isinstance(limit, int):
        print("limit must be an integer")
        return 1
    if limit <= 0:
        print("limit must be a positive integer")
        return 2
    longest_collatz_length = 0
    longest_collatz_starter = 0
    for num in range(1, limit + 1):
        num_li = []
        recursive_collatz(num, num_li)
        if len(num_li) > longest_collatz_length:
            longest_collatz_length = len(num_li)
            longest_collatz_starter = num_li[0]
    print(f'The longest Collatz length with a starting value under {limit} '
          f'is {longest_collatz_length} numbers long and starts with {longest_collatz_starter}')
    return 0


longest_collatz_sequence(14)
