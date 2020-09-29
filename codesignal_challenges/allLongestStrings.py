"""
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):

    answer = [inputArray[0]]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) == len(answer[0]):
            answer.append(inputArray[i])
        if len(inputArray[i]) > len(answer[0]):
             answer = [inputArray[i]]  # Need to update the answer list with the most max chars
    return answer

# inputArray = ["aba", "aa", "ad", "vcd", "aba"]
# inputArray = ["abc", "eeee", "abcd", "dcd"]
inputArray = ["a", 
            "abc", 
            "cbd", 
            "zzzzzz", 
            "a", 
            "abcdefjdjdjdjbfjbdfjbjgfr",
            "abcdefjdjdjdjbfjbdfjbjgfr", 
            "asasa", 
            "aaaaaa",
            "zzzzzzzzzzzzzzzzzz"]

if __name__ == "__main__":
    print(allLongestStrings(inputArray))


############################   Couldn't figure it out   ###########################3