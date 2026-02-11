from functools import reduce

def symmetric_function(list1, list2):
    output_list = []
    for value in list1:
        if value not in list2 and (value not in output_list):
            output_list.append(value)
    for value in list2:
        if value not in list1 and (value not in output_list):
            output_list.append(value)
    return output_list


def symmetric_difference(*args):
    list_of_lists = [*args]
    out_list = reduce(symmetric_function, list_of_lists)
    out_list.sort()
    return out_list


# Uses reduce to apply the first function to every element of the list of lists that was provided. This is
# because, as the problem descibes, the correct way to do the math here is to find the difference between
# the first two lists, then the difference between that new list and the third list, and so on. 
