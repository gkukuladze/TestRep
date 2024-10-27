def fibonacci_sequence(n):
    
    if n <= 0:
        return "გთხოვთ შეიყვანოთ დადებითი მთელი რიცხვი"
    
    sequence = [0, 1]
    
    if n == 1:
        return [0]
    
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence

n = 10
print(fibonacci_sequence(n))  
