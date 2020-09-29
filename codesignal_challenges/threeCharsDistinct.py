"""
You are given a string string, which consists only of lowercase English letters. 
Your task is to find the number of adjacent triplets of unique characters within string. 
In other words, count the number of indices i, such that string[i], string[i + 1], and string[i + 2] 
are all pairwise distinct.

Example

For s = "abcdaaae", the output should be threeCharsDistinct(s) = 3.

If i = 0, s[0] = 'a', s[1] = 'b', and s[2] = 'c', which are pairwise distinct;
If i = 1, s[1] = 'b', s[2] = 'c', and s[3] = 'd', which are pairwise distinct;
If i = 2, s[2] = 'c', s[3] = 'd', and s[4] = 'a', which are pairwise distinct;
If i = 3, s[3] = 'd', s[4] = 'a', and s[5] = 'a', which are not pairwise distinct because s[4] and s[5] are equal;
If i = 4, s[4] = 'a', s[5] = 'a', and s[6] = 'a', which are not pairwise distinct because all pairs of characters are equal;
If i = 5, s[5] = 'a', s[6] = 'a', and s[7] = 'e', which are not pairwise distinct because s[5] and s[6] are equal.
If i = 6 or i = 7, at least one of characters s[i + 1] or s[i + 2] won't exist.
For s = "abacaba", the output should be threeCharsDistinct(s) = 2.

There are only 2 indices meeting the criteria:

i = 1: s[1] = 'b', s[2] = 'a', and s[3] = 'c';
i = 3: s[3] = 'c', s[4] = 'a', and s[5] = 'b'.
All other triplets will contain more than one a character.
"""
############################################### My Attempt  #########################################################

# def threeCharsDistinct(string):

#     unique_chars = ''.join(set(string))
#     # Parse the string 
#     # for char in range(0, len(unique_chars), 3):
#     # Identify unique characters
#         # unique_chars[char:char + 3]
#         # print(char)
#     # Print pariwise of each unique character
#     print("Unique Characters: ", unique_chars)
#     threeChars = [unique_chars[char:char + 3] for char in range(0, len(unique_chars), 3)][0]
#     return len(threeChars), threeChars

# if __name__ == "__main__":
#     string = "abacabadeddde"
#     print(threeCharsDistinct(string))

#############################################################################################################

def threeCharsDistinct(string):
    unique_char = 0
    for i in range(2, len(string)):
        if string[i] != string[i-1] and string[i] != string[i-2] and string[i-2] != string[i-1]:
            unique_char += 1
    return unique_char

if __name__ == "__main__":
    string = "abacabadeddde"
    print(threeCharsDistinct(string))