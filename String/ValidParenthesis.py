from operator import truediv


def valid_parenthesis(str):
    stack = []
    for s in str:
        if s in ('[', '(', '{'):
            stack.append(s)
        if s == ']':
            peek_element = stack[-1]
            if peek_element == '[':
                stack.pop()
        if s == ')':
            peek_element = stack[-1]
            if peek_element == '(':
                stack.pop()
        if s == '}':
            peek_element = stack[-1]
            if peek_element == '{':
                stack.pop()

    if not stack:
        return True
    else:
        return False


print(valid_parenthesis("()[]{}"))
print(valid_parenthesis("(]"))
print(valid_parenthesis("([])"))
