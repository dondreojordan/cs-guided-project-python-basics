"""
Reverse the order of words in a given string sentence. You can assume that sentence does not have any leading, trailing or repeating spaces.

Example

For sentence = "Man bites dog", the output should be
reverseSentence(sentence) = "dog bites Man".
"""


# def reverseSentence(sentence):  
#     # first split the string into words 
#     words = sentence.split(' ')  
#     print(words)
#     # then reverse the split string list and join using space 
#     reverse_sentence = ' '.join(reversed(words))  

#     # finally return the joined string 
#     return reverse_sentence  

def reverseSentence(sentence):   
    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence

#Another way to do it
# def reversedSentence(sentence):
#     return "".join(sentence.split()[::-1])

if __name__== "__main__":
    sentence = "Old man bites dog and laughed"
    print(reverseSentence(sentence))