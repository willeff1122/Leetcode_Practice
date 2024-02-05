class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {')' : '(', ']' : '[', '}' : '{' }
        for p in s:
            if p in pmap:
                if stack and stack[-1] == pmap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if not stack else False