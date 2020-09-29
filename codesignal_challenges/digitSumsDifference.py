"""
Given an integer n, find the difference between the sums of its even and odd digits.

Example

For n = 412, the output should be
digitSumsDifference(n) = 5;
For n = 1203, the output should be
digitSumsDifference(n) = -2.
"""

# def digitSumsDifference(n):
    # Input: n, an int of anywhere from single to multi-digit unit
    # Need to parse n (int) into single digit int form
    # If % 2 == 1 (remainder equals 1), then odd and append to odd list; otherwise, even and append to even list.

    # Recap: given n, what is the difference (subtraction) of the sum of the group of even numbers minut the sum of the group of odd numbers
    # return: the difference of even from odd numbers.
    # return
def digitSumsDifference(n):
    numbers = [int(i) for i in str(n)]
    
    even = 0
    odd = 0
    for num in numbers:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return even - odd


if __name__ == '__main__':
    n = 1203
    print(digitSumsDifference(n))
