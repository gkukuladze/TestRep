from functools import reduce

def multiply_list_elements(lst):
    try:
        return reduce(lambda x, y: x * y, lst)
    except TypeError:
        return "Error: List should contain only numbers."

numbers = [1, 2, 3, 4, 5]
result = multiply_list_elements(numbers)
print(result)
