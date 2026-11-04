class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        stack = []
        for c in s:
            if c not in dct:
                stack.append(c)
            elif len(stack)!=0 and dct[c] == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) > 0:
            return False
        return True