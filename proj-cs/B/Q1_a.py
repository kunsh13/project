def vovelLine():
    with open("C:/Users/kunsh/Downloads/proj-cs/B/Content.txt","r")as file:
        line=1
        count=0
        for i in file:
            
            file1=file.readline()
            for j in file1:

                if j.lower() in "aeiou":
                    count+=1
                # print(file1,line)
                    line+=1
            print(count)
                     

            

           


vovelLine()
