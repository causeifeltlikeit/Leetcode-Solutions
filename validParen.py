stack = []
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            return False
        popped = stack.pop()
        if (popped == '(' and i != ')') or (popped == '{' and i != '}') or (popped == '[' and i != ']'):
            return False
return len(stack) == 0