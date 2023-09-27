stack = []
odd_stack = []
even_stack = []

def push(item):
    stack.append(item)
    if item % 2 == 0:
        even_stack.append(item)
    else:
        odd_stack.append(item)

def print_st():
    if not stack:
        print("Stack is empty")
    else:
        print("Elements in stack:")
        for item in stack:
            print(item)

while True:
    try:
        num = int(input("Enter some numbers or 0 to leave: "))



        if num == 0:
            break

        push(num)
    except ValueError:
        print("Error")


print("Stack with even numbers: ")
for item in even_stack:
    print(item)
print("Stack with odd numbers: ")
for item in odd_stack:
    print(item)
print_st()
    
            
