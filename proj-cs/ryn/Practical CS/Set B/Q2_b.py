Stack = []

def push(elem):
    Stack.append(elem)
    return elem

def pop():
    return Stack.pop()

# take input as long as user wants to continue and provide push pop and view options
while True:
    print("1. Push")
    print("2. Pop")
    print("3. View")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        elem = [input("Enter rollno: "), input("Enter name: "), input("Enter marks: ")]
        print(push(elem))
    if choice == 2:
        print("Popped element: ", pop())
    if choice == 3:
        print("Stack: ", Stack)
    if choice == 4:
        break
