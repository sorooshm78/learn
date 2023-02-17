def my_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + my_sum(numbers[1:])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = my_sum(numbers)
print(sum)

#############################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

avg = my_sum(numbers) / len(numbers)
print(avg)


##############################


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibo(n - 1) + fibo(n - 2)


f = fibo(5)
print(f)
