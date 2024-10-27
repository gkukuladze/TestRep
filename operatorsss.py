num1 = int(input("შეიყვანე პირველი რიცხვი: "))

total_sum = 0

if num1 >= 0:
    total_sum += num1
    num2 = int(input("შეიყვანე მეორე რიცხვი: "))
    if num2 >= 0:
        total_sum += num2
        num3 = int(input("შეიყვანე მესამე რიცხვი: "))
        if num3 >= 0:
            total_sum += num3
            print("ჯამი არის (total_sum)")
        else:
            print("მესამე რიცხვი არის უარყოფითი ")
    else:
        print("მეორე რიცხვი არის უარყოფითი")
else:
    print("პირველი რიცხვი არის უარყოფითი")
    