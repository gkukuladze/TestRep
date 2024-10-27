file1_name = "file1.txt"
file2_name = "file2.txt"
gaertianebuli_file_name = "gaertianebuli_file.txt"

with open(file1_name, "r") as file1, open(file2_name, "r") as file2:
    content1 = file1.read() 
    content2 = file2.read() 

with open(gaertianebuli_file_name , "w") as gaertianebuli_file:
    gaertianebuli_file.write(content1)  
    gaertianebuli_file.write(content2)  

with open(gaertianebuli_file_name, "r") as output_file:
    gaertianebuli_content = output_file.read()  

print("გაერთიანებული ფაილის შინაარსი:")
print(gaertianebuli_content)