'''Factorial is a mathematical task represented by the exclamation sign ("!"). It represents the product of an
integer and all the integers below it. Per its definition, factorial only involves POSITIVE integers 
(no negative or float point values)'''

def factorial(n):
    # First step: ensure the input is a positive integer, else raise an exception
    try:
        if isinstance(n, int) == False or n < 0:
            raise ValueError
    except ValueError:
        print('ERROR! Factorial only accepts positive integer values')
    # Second: calculate the product of the integer and all integers below it
    else:
        # create a variable x to hold the product of all integers in n
        x = 1
        # for-loop to iterate all integers in range 1 to n
        for i in range(1, n + 1):
            # get the product of all integers found in the for-loop and save them in x
            x *= i
        return x
