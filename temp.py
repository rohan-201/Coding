def push(s, val):
    s.append(val)

def pop(s):
    if not s:  # Use Pythonic way to check if the stack is empty
        print('Stack is empty::')
    else:
        val1 = s.pop()
        print('Item to be deleted is::', val1)

def display(s):
    
    if not s:
        print('Stack is empty')
    else:
        print('Stack contents:', s)

s = []
while True:
    print('1. Press 1 for Insertion or push operation::::')
    print('2. Press 2 for Deletion or pop operation::::')
    print('3. Press 3 for displaying the values of stack:::::')
    print('4. Press 4 to quit the program::::::::::::')
    ch = int(input('Enter your choice of operation to be performed::::::'))
    if ch == 1:
        val = int(input('Enter item to be inserted:::::'))
        push(s, val)
    elif ch == 2:  # Use `elif` for better structure
        pop(s)
    elif ch == 3:
        display(s)
    elif ch == 4:
        break
    else:
        print("Invalid choice, please try again.")
