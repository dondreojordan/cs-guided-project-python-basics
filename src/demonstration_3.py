"""
Write a function that takes in a two-dimensional list (a list that contains
lists) and returns a new list which contains only the lists from the original
which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or
strings. Also, for this challenge, we are assuming that empty arrays are not
homogenous. Also, the resultant lists should be in the same order as the
original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should
return `[[1, 5, 4], ['b']]`.
"""
####################################   My Attempt, FIX   #####################################################
def filter_homogen(arrays):
    """List should be multi-dimensional"""
    to_return = []
    for list_ in arrays:
        item = None
        same_type = True
        for i in list_:
            if item is None:
                item = i
            if i is not item and type(i) is not type(item):
                same_type = False
        if same_type and len(list_) != 0:
            to_return.append(list_)
    return to_return

def filter_homogenous(arrays):
    return [i for i in arrays if i != [] and all(type(j) == type(i[0]) for j in i)]
###########################################################################################################
if __name__ == '__main__':
    arrays = [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3],
              ['e', 'u'], [1, 856,'e'], [8], [], [21, 52, 'p']]
    print("Function One: ", filter_homogenous(arrays))
    print("Function Two: ", filter_homogen(arrays))

