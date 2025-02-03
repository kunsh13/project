def push():
    stack=[]
    l1=[1001,"Shweta",25,"Dr.PSingh"]
    l2=[1002,"Ricky",34,"Dr.LGoyal"]
    stack.append(l1)
    stack.append(l2)
    print(stack)
    return stack
    

def pop(stack):
    if stack ==[]:
        print("stack empty")

    else:
        a=stack.pop()
        print(a)



stack = push()
pop(stack)