"""
Given a positive integer number n, your task is to calculate the difference between the product of its digits and the sum of its digits.

Note: The order matters; the answer should be of the form product - sum (and not sum - product).

Example

For n = 123456, the output should be digitsManipulations(n) = 699.

The product of the digits is equal to 1 * 2 * 3 * 4 * 5 * 6 = 720.
The sum of the digits is equal to 1 + 2 + 3 + 4 + 5 + 6 = 21.
So the final answer is 720 - 21 = 699.

For n = 1010, the output should be digitsManipulations(n) = -2.

The multiplication of the digits is equal to 1 * 0 * 1 * 0 = 0.
The sum of the digits is equal to 1 + 0 + 1 + 0 = 2.
So the final answer is 0 - 2 = -2.
"""

# def digitsManipulations(n):
    # input: positive int containing single to multi-digit int
    # split n into single digit ints
    # take all numbers and multiply
    # take all numers and get the sum
    # return: the difference between the product of its digits and the sum of its digits
    # return

def digitsManipulations(n):
    numbers = [int(i) for i in str(n)]
    product = 0
    sum_ = 0
    for num in numbers:
        sum_ += num
        if product == 0:
            product += num
        else:
            product *= num

    return product - sum_


if __name__ =='__main__':
    # n = 123456
    n = 80
    print(digitsManipulations(n))
