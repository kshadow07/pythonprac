def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)

        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False   
    return not stack

print(isValid("()"))




    