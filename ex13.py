# ask for number of Fib numbers to generate; then generate them

num = int(input('How many numbers of the Fibonacci sequence should I print out?: '))
fib_nums = []

def fibonacci_to_nth_place(n):
    def fib(number):
        if (number == 0 or number == 1):
            return 1
        else:
            return fib_nums[number-2] + fib_nums[number - 1]

    for i in range(n):
        fib_nums.append(fib(i))


fibonacci_to_nth_place(num)
print(fib_nums)