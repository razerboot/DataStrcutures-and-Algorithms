
stack = []

def is_empty(stack):
    return len(stack)==0

def last(stack):
    if is_empty(stack):
        return False
    return stack[-1]

def pop(stack):
    if is_empty(stack):
        return False
    return stack.pop(-1)

def sort(stack):
    