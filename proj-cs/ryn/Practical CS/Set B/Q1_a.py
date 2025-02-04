def vowelLine():
    file = open("Content.txt", "r")
    for line in file.readlines():
        count = 0
        for char in line:
            if char in "aeiouAEIOU":
                count += 1
        print("Number of vowels in line:", count)

vowelLine()
