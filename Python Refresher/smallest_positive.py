def smallest_positive(in_list):
    smallest = in_list[0]
    for num in in_list:
        if num > 0:
            if num < smallest:
                smallest = num
    return smallest

print(smallest_positive([4, -6, 7, 2, -4, 10]))
print(smallest_positive([0.2, 5, 3, -1, 7, 7, 6]))