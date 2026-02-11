def merge_lists(lists):
    flat_list = [x for y in lists for x in y]
    flat_list.sort()
    return flat_list


print(merge_lists([[1, 2], [8, 9], [3, 4]]))
