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
