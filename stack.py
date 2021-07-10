# A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
# This means the last element inserted inside the stack is removed first.

# Create a stack
def create_stack():
    stack = []
    return stack

# Check a stack
def check_stack(stack):
    if len(stack) == 0:
        print("stack is Empty")

    print("stack: ", stack)
    
# removing item from stack
def pop(stack):
    if len(stack) == 0:
        print("stack is Empty")
    else:  
        remove = stack.pop()
        print("remove element is:", remove)
    
# Adding values into the stack
def push(stack, value):
    stack.append(value)
    print("Push elemet is:", value)
    
stack = create_stack()
push(stack, 400)
push(stack, 100)
push(stack, 200)
push(stack, 300)
pop(stack)
check_stack(stack)

# Stack Time Complexity => 0(1)
    
    