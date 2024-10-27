from functools import filter

get_positive_numbers = lambda lst: list(filter(lambda x: x > 0, lst))

numbers = [-5, 3, -2, 8, -1, 7, 0]
positive_numbers = get_positive_numbers(numbers)
print(positive_numbers)
