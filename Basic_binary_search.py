"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math
def binary_search(input_array, value):
    """Your code goes here."""
    temp_arr = input_array
    while True:
        l = len(temp_arr)
        if l%2:
            k = math.floor(l/2)
        else:
            k = math.floor(l/2) - 1
        k = int(k)
        if value < temp_arr[k]:
            if k != 0:
                if k != 1:
                    temp_arr = temp_arr[:k-1]
                else:
                    temp_arr = temp_arr[:1]
            else:
                break
        elif value > temp_arr[k]:
            if k != 0:
                temp_arr = temp_arr[k+1:]
            else:
                break
        else:
            return input_array.index(value)



    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

