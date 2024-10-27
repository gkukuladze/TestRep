def zip_lists(list1, list2):
    zipped = zip(list1, list2)
    
    result = [f"({x}, '{y}')" for x, y in zipped]
    
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

output = zip_lists(list1, list2)
print(output)
