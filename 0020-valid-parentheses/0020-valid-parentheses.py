class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for item in s:
            if item=='(' or item=='[' or item=='{':
                stack.append(item)
                
            if item==')':
                if stack:
                    temp = stack.pop()
                    if temp != '(':
                        return False
                else:
                    return False
            if item==']':
                if stack:
                    temp = stack.pop()
                    if temp != '[':
                        return False
                else:
                    return False
            if item=='}':
                if stack:
                    temp = stack.pop()
                    if temp != '{':
                        return False
                else:
                    return False
           
            
        if not stack:
            return True
        else:
            return False

        