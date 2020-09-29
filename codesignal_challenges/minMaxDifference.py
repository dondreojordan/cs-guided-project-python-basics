"""
There is a bug in one line of the code. Find it, fix it, and submit.
Given an array, find the absolute difference between its minimal and maximal elements.

Example

For inputArray = [1, 4, 10, 4, 2], the output should be
minMaxDifference(inputArray) = 9.

Here |10 - 1| = 9.
"""
def minMaxDifference(inputArray):

    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(0, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMaximum]:
            indexOfMaximum = i
    return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]

if __name__ == "__main__":
    inputArray = [1, 4, 10, 4, 2]
    inputArray2 = [32, 19, 11, 23]
    print("First Array: ", minMaxDifference(inputArray))
    print("Second Array: ", minMaxDifference(inputArray2))