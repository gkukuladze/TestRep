def filter_by_ending(lst, ending):
    try:
        return list(filter(lambda s: s.endswith(ending), lst))
    except TypeError:
        return "Error: The first parameter should be a list of strings, and the second parameter should be a string."

strings = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
result = filter_by_ending(strings, ending)
print(result)
