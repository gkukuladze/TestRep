def split_file_into_groups(filename):
    with open(filename, "r") as file:
        lines = file.readlines() 

    for i in range(0, len(lines), 10):
        group_number = i // 10 + 1 
        with open(f"group_{group_number}.txt", "w") as new_file:
            new_file.writelines(lines[i:i + 10])  
            
split_file_into_groups("my_file.txt") 