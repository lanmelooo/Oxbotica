def calculate() -> 'str':
    """
    Write a solution in the most concise way possible in a programming language of your choice. Write a short program
        that prints each number from 1 to 100 on a new line. For each multiple of 3, print ‘Fizz’ instead of the number.
        For each multiple of 5, print ‘Buzz’ instead of the number. For numbers which are multiples of both 3 and 5,
        print ‘FizzBuzz’ instead of the number.
    """
    for num in range(1, 101):
        string = ''
        if num % 3 == 0:
            string = string + 'Fizz'
        if num % 5 == 0:
            string = string + 'Buzz'
        if num % 5 != 0 and num % 3 != 0:
            string = string + str(num)
        # else:
        #     return ''
        print(string)
