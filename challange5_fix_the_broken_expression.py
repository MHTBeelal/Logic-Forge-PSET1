def remove_invalid_parentheses(s):
    result = set()

    # first count misplaced '()' and ')'
    leftrm = rightrm = 0
    for ch in s:
        if ch == '(':
            leftrm += 1
        elif ch == ')':
            if leftrm == 0:
                rightrm += 1
            else:
                leftrm -= 1

# applying Depth First Search
    def dfs(index, left_count, right_count, lrm, rrm, path):
        # If end is reached
        if index == len(s):
            if lrm == 0 and rrm == 0:
                result.add(path)
            return

        ch = s[index]
    
        # Option 1: Remove '('
        if ch == '(' and lrm > 0:
            dfs(index + 1, left_count, right_count, lrm - 1, rrm, path)
    
        # Option 2: Remove ')'
        elif ch == ')' and rrm > 0:
            dfs(index + 1, left_count, right_count, lrm, rrm - 1, path)
    
        # Option 3: Keep the current character
        if ch not in '()':
            dfs(index + 1, left_count, right_count, lrm, rrm, path + ch)
        elif ch == '(':
            dfs(index + 1, left_count + 1, right_count, lrm, rrm, path + ch)
        elif ch == ')' and right_count < left_count:
            dfs(index + 1, left_count, right_count + 1, lrm, rrm, path + ch)
    
    dfs (0, 0, 0, leftrm, rightrm, "")
    return list(result)

expr = input("Input: ")    
print("Output:", remove_invalid_parentheses(expr), "\n")   
