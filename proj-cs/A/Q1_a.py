def search():
    with open("myfile.txt","r")as file:
        file=file.read()
        file=file.split()
        count=0
        for i in file:
            if i.lower() =="the" or i.lower() =="than":
                count+=1
        return count
    
print(search())

        