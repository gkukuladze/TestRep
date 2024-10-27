with open("selected_lines.txt", "w") as file:
    for i in range(1, 18): 
        if i == 2:
            file.write("მეორე ხაზი\n")
        elif i == 8:
            file.write("მერვე ხაზი\n")
        elif i == 10:
            file.write("მეათე ხაზი\n")
        elif i == 13:
            file.write("მეცამეტე ხაზი\n")
        elif i == 17:
            file.write("მეჩვიდმეტე ხაზი\n")
        else:
            file.write("\n")