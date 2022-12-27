def match(text):
    if text is None:
        return 0
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    stack = []
    for char in text:
        if char in open_brackets:
            stack.append(char)
            continue
        if char in close_brackets:
            if len(stack) == 0:
                return 1
            peek = stack.pop()
            if close_brackets.index(char) != open_brackets.index(peek):
                return 1

    return 0 if len(stack) == 0 else 1


print(match("[{[[[(())]]]}]"))
print(match(None))
print(match("{)"))
print(match("{([)]}"))
