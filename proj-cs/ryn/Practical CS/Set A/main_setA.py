# Q1  a)
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

# Q2 b)
Stack = []

def push(elem):
  Stack.append(elem)
  return elem

def pop():
  if len(Stack) == 0:
    print("Stack is empty")
  else:
    return Stack.pop()

while True:
  menu = int(input("1 - push\n2 - pop\n3 - view\nEnter your choice: "))
  if menu == 1:
    elem = [int(input("Enter patient id: ")), input("Enter name: "), int(input("Enter age: ")), input("Enter doctor: ")]
    push(elem)
  elif menu == 2:
    print(pop())
  elif menu == 3:
    print(Stack)
  else:
    break
