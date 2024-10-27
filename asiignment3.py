number1 = int(input("შეიყვანეთ პირველი რიცხვი: "))


number2 = int(input("შეიყვანეთ მეორე რიცხვი:"))


operator = input("შეიყვანეთ ოპერატპორი(+, -, *, /): ")


if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("ნულზე გაყოფა არ შეიძლება.")
else:
    print("არასწორი ოპერატორი.")