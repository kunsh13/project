def push():
    stack=[]
    l1=[101,"Garima",25]
    l2=[102,"Richa",24]
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