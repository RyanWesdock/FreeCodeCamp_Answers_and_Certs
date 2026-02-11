# https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/24-game
# Program which correctly generates properly formatted strings representing an equation of integers 1 - 9
# that ultimately equals 24. This does not work for [3, 3, 8, 8].

import itertools
import re

# Performs all operations on two variables. y (operator) x situations are covered by permutations of the variable list


def all_operations_two(x: float, y: float, switch=0):
    operations_list = list()
    if switch == 0:
        operations_list.append((x + y, f'{x}+{y}'))
        operations_list.append((x - y, f'{x}-{y}'))
        operations_list.append((x * y, f'{x}*{y}'))
        try:
            operations_list.append((x / y, f'{x}/{y}'))
        except ZeroDivisionError:
            pass
    elif switch == 1:  # Because for proper formatting, I need only to include the new operation.
        operations_list.append((x + y, f'+{y}'))
        operations_list.append((x - y, f'-{y}'))
        operations_list.append((x * y, f'*{y}'))
        try:
            operations_list.append((x / y, f'/({y})'))
        except ZeroDivisionError:
            pass
    return operations_list

# Performs all operations on three variables. Like in the function above, situations with the parameters in different
# order (e.g. x (operator) z (operator) y) are covered by iterating through all permutations of the arguments below.


def all_operations_three(x: float, y: float, z: float):
    operations_list = list()
    # adding z block
    operations_list.append((x + y + z, f'{x}+{y}+{z}'))
    operations_list.append((x - y + z, f'{x}-{y}+{z}'))
    operations_list.append((x * y + z, f'{x}*{y}+{z}'))
    # subtracting z block
    operations_list.append((x + y - z, f'{x}+{y}-{z}'))
    operations_list.append((x - y - z, f'{x}-{y}-{z}'))
    operations_list.append((x * y - z, f'{x}*{y}-{z}'))
    # multiplying z block
    operations_list.append((x + y * z, f'{x}+{y}*{z}'))
    operations_list.append((x - y * z, f'{x}-{y}*{z}'))
    operations_list.append((x * y * z, f'{x}*{y}*{z}'))
    # dividing z block
    try:
        operations_list.append((x + y / z, f'{x}+{y}/{z}'))
        operations_list.append((x - y / z, f'{x}-{y}/{z}'))
        operations_list.append((x * y / z, f'{x}*{y}/{z}'))
        operations_list.append((x / y / z, f'{x}/{y}/{z}'))
    except ZeroDivisionError:
        pass
    return operations_list


# Takes a list of integers (1 - 9 inclusive). A list of all permutations of this list is created and made into a
# dictionary with the permutations as keys in order to eliminate duplicates.
par_vars = [9, 4, 1, 3]
par_vars_dict = {item: None for item in list(itertools.permutations(par_vars))}

# Function for structure (a b) (c d)
for tupper in par_vars_dict:
    a, b, c, d = tupper
    for tupper1 in all_operations_two(a, b):
        nums1, st1 = tupper1
        for tupper2 in all_operations_two(c, d):
            nums2, st2 = tupper2
            for tupper3 in all_operations_two(nums1, nums2):
                nums3, st3 = tupper3
                if nums3 == 24:
                    new_st3 = re.sub(r'[0-9a-z\s.]*', "", st3)  # This isolates the operator
                    new_st3 = re.sub(r'\+-|-\+', "+", new_st3)  # This resolves issues with negative numbers
                    print(f'({st1}){new_st3}({st2})')


# Function for structure (a b c) d. From testing, this also includes (a) (b) (c) (d).
for tupper in par_vars_dict:
    a, b, c, d = tupper
    for tupper1 in all_operations_three(a, b, c):
        nums1, st1 = tupper1
        for tupper2 in all_operations_two(nums1, d):
            nums2, st2 = tupper2
            if nums2 == 24:
                new_st2 = re.sub(r".*(?=[*+/-])", "", st2)  # needed to isolate the operator between the ()
                print(f'({st1}){new_st2}')
