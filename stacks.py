def is_balanced(expression):
    opening = []
    condition = True

    if len(expression) % 2 != 0:
        return False

    for char in expression:
        if condition:
            if char in "[{(":
                opening.append(char)
            elif char in "]})": 
                last = opening.pop()           
                if char == "}":
                    condition = last == '{'
                    
                elif char == "]":
                    condition = last == '['
                elif char == ")":
                    condition = last == '('
            
    return condition

expression1 = "()][{}"
expression2 = "([)??]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 
