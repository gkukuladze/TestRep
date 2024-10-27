def remove_empty_lines(input_file, output_file):
    with open(input_file, "r") as file: 
        all_lines = file.readlines()  

    filled_lines = [] 
    for line in all_lines: 
        if line.strip(): 
            filled_lines.append(line)  


    with open(output_file, "w") as file:  
        file.writelines(filled_lines)  

    print(f"უკვეცარიელი ხაზები ამოიშლილია და ინფორმაცია {output_file} ფაილში ჩაიწერა.")


remove_empty_lines("input_file.txt", "output_file.txt") 