"""
There is a bug in one line of the code. Find it, fix it, and submit.
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):

    answer = ['']

    for i in range(len(picture[0])+2):
        answer[0] += '*'
        print(answer[0])
    for i in range(len(picture)):
        answer.append('*')
        for j in range(len(picture[0])):
            answer[i + 1] += picture[i][j]
            # print(answer)
        answer[i + 1] += '*'
        # print(answer)

    answer.append(answer[0])

    return answer

if __name__ == "__main__":
    picture = ["abc",
            "ded"]
    print(addBorder(picture))
    # print(len(picture[0]))