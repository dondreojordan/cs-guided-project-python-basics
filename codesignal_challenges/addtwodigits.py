"""
For n = 29, the output should be
addTwoDigits(n) = 11.
"""

def addTwoDigits(n):
    return int(str(n)[0]) + int(str(n)[1])

if __name__ == "__main__":
    n = 10
    print("Practice print statement", str(n)[0] + str(n)[1])
    print(addTwoDigits(n))