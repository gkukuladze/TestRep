get_even_numbers = lambda lst: [x for x in lst if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
