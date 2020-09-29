"""
You are given a string s that consists of only lowercase English letters. If vowels ('a', 'e', 'i', 'o', and 'u') are given a value of 1 and 
consonants are given a value of 2, return the sum of all of the letters in the input string.

Example

For s = "a", the output should be
countVowelConsonant(s) = 1;

For s = "abcde", the output should be
countVowelConsonant(s) = 8.

The letters in s, converted to 1s and 2s and added together as described above: 1 + 2 + 2 + 2 + 1 = 8.
"""

# def countVowelConsonant(s):
    # input: s, str containing lowercase vowels and consonants
    # Determine what letters are a vowel ('a', 'e', 'i', 'o', and 'u')
    # Split string into letters
    # Loop letters in string and determine if it is a vowel
    # Keep updated count
    #return: the sum of all of the letters. values == 1, and consonants == 2
    # return
##############################################################  My First Attempt  #########################################
# def countVowelConsonant(string):
#     string = string.lower() 
#     s_split = [char for char in string] 
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     total = 0
#     # for word, letter in [(word, letter) for word in s_split for letter in vowels]:
#     for word in s_split:
#         print("word", word)
#         for letter in vowels:
#             print("letter", letter)
#             if  word == vowels:
#                 total += 1
#             else:
#                 total += 1

#     return total
# Second Attempt
# def countVowelConsonant(string):
#     s_split = [char for char in string] 
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     total = 0
#     for char in s_split:
#         if char != vowels:
#             total += 2
#         else:
#             total += 1

#     return total
###########################################################################################################################
def countVowelConsonant(string):
    string = string.lower()
    s_split = [char for char in string]
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counts = []
    for vowel in vowels:
        count = s_split.count(vowel)
        if count == 1:
            vowel_counts.append(count)
        else:
            vowel_counts.append(2)
    abc = sum(vowel_counts)
    return abc

if __name__ == '__main__':
    # string = "a"
    # string = "AbCdE"
    string = "oqaawtnkqo"
    print(countVowelConsonant(string))