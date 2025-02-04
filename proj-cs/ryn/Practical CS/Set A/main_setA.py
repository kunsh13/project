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
  '''
def isempty (stk):
    if stk == []:
        return True
    else:
        return False
def Push(stk,elt):
    stk.append(elt)
    print("element added successfully")
    print(stk)
def Pop(stk):
    if isempty(stk) :
        print("stack is empty......UNDERFLOW")
    else:
        print("popped element is ", stk.pop())
def peek(stk):
    if isempty(stk):
        print("stack is empty top none!!!!")
    else:
        print("element at the top ", stk[-1])
def display(stk):
    print(stk[::-1])
        
        
Stack = [ ]
while True:
     print("..........Stack Implementation............")
     print(" 1.Push")
     print("2.POP")
     print("3.peek")
     print("4.display")
     print("5 EXIT")
     ch = int(input("enter your choice"))
     if ch == 1:
          element = [input("Enter rollno: "), input("Enter name: "), input("Enter marks: ")]
          Push(Stack,element)
     elif ch == 2:
             Pop(Stack)
     elif ch == 3:
         peek(Stack)
     elif ch == 4:
             display(Stack)
         
     elif ch == 5:
         break
    '''
    
         
     
     
     

