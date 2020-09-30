"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""

string = "supercalifragilisticexpialidocious"
part_length = 3


# def split_in_parts(string, part_length):
    # Your code here
    # we need to split the input string into smaller chunks into a specified size

    #init an output array  

    # iterate characters in the input string

        # keep a counter that will count up to 'part_length' characters
        # once our counter == 'part_length'
            # then we've collected enough chars for a single substring
            # add that collected substring to an array 

            # start counter over again
            # Not sure this works with the instructions

        # otherwise
            # increment our counter
            # add the current character to the substring we're building up

    # This function should output an array
    # return # our array


# One way to build code
def split_in_parts(string, part_length):
    output = []
    for i in range(0, len(string), part_length):
        # print(i)
        output.append(string[i: i + part_length])
        print(i, string[i:i+part_length])
    return output

# Call function
print(split_in_parts(string, part_length))
print()
# Another way to build code
def split_by_parts(string, part_length):
    return [string[i:i + part_length] for i in range(0, len(string), part_length)]


if __name__ == '__main__':
    # Call function
    print(split_by_parts(string, part_length))