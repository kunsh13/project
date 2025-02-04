def count_the_this():
  f = open("myfile.txt", "r")
  count_the = 0
  count_this = 0

  content = f.read().split()
  for i in content:
    if i.lower() == "the":
      count_the += 1
    elif i.lower() == "this":
      count_this += 1
  print("The count of 'the' is: ", count_the)
  print("The count of 'this' is: ", count_this)

count_the_this()
