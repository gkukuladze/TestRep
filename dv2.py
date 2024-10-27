
total_sum = 0

while True:
    user_input = input("შეიყვანეთ რიცხვი ან ტექსტი 'sum' ჯამის დასათვლელად: ")
    
    if user_input.lower() == "sum":
        break
    
    try:
        number = float(user_input)
        
        if number > 0:
            total_sum += number
    except ValueError:
        print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი ან 'sum' ჯამის დასათვლელად.")

print(f"დადებითი რიცხვების ჯამი არის: {total_sum}")
