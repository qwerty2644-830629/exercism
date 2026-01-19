def is_paired(input_string):
    PAIRS = {'(': ')', '[': ']', '{': '}'}    
    stack = [] # stack

    for char in [i for i in input_string if i in "()[]{}"]: # char only in "()[]{}"
        print(stack)
        if char in "([{": # push
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0 or PAIRS[stack.pop()] != char:# stack = []
                return False # or stack[-1] != char
            

    return not stack # stack = [] -> True