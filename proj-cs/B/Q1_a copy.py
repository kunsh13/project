def vovelLine():
    with open("Content.txt","r")as file:
        count=0
        file=file.read()
        file=file.split()

        for i in file:
            if i.lower() in "aeiou":
                count+=1
        print(count)


vovelLine()
