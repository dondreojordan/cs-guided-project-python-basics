"""
You have been asked to implement a line numbering feature in a text editor that
you are working on.

Write a function that takes a list of strings and returns a new list that
contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make
sure to put a colon and space in between the `line_number` and `string` value.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""
#########################################   My Attempt, FIX    ###############################################
# line_number = [1, 2, 3, 4]
# string_value = ["a", "b", "c", "d"]
# def number(list_values):

#     # Create an empty list for numbers
#     numbers = []
#     # Create a for loop that takes the indeces of list_values and puts the line_number in front, seperated by a ":"
#     for i in range(0, len(string_value)):
#         numbers.append(i+1)
#     # When you have two lists, insert in indexed position (not i +1) with the semi-colon":" 
#         string_value.insert(i, numbers[i])


#     return string_value
#     # Returns a list (e.g. ["1: a", "2: b", "3: c"]) 

# print(number(string_value))
############################################################################################################
string_value = ["a", "b", "c", "d"]
# # One Way
def number(lines):
    output = []
    line_number = 1
    for line in lines:
        output.append(f"{line_number}: {line}")
        line_number += 1

    return output
print("First Function", number(string_value))


# Second Way
def numbers(lines):
    output = []
    for index, line in enumerate(lines):
        output.append(f"{index + 1}: {line}")
    return output


if __name__ == '__main__':
    print("Second Function", numbers(string_value))