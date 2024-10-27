import random


random_number = random.randint(1, 100)


lives = 5


while lives > 0:
    
    try:
        guess = int(input("გამოიცანით რიცხვი 1-დან 100-მდე: "))
    except ValueError:
        print("გთხოვთ, შეიყვანოთ მხოლოდ რიცხვი.")
        continue

    if guess > random_number:
        print("თქვენი რიცხვი მეტია.")
    elif guess < random_number:
        print("თქვენი რიცხვი ნაკლებია.")
    else:
        print(f"გილოცავთ! თქვენ გამოიცანით სწორი რიცხვი: {random_number}")
        break
    
    lives -= 1
    print(f"დარჩენილი სიცოცხლე: {lives}")

else:
    print(f"სამწუხაროდ, სიცოცხლე ამოგეწურათ. სწორი რიცხვი იყო: {random_number}")
