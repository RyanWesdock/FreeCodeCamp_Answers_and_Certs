# Needs to return an array of integers between 1 and 100 where multiples
# of three are returned as "Fizz" and multiples of 5 returned as "Buzz"
# and multiples of three AND five are returned as "FizzBuzz"
def fizzbuzz():
    fizz_list = []
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            fizz_list.append("FizzBuzz")
        elif x % 3 == 0:
            fizz_list.append("Fizz")
        elif x % 5 == 0:
            fizz_list.append("Buzz")
        else:
            fizz_list.append(x)
    return fizz_list


print(fizzbuzz())