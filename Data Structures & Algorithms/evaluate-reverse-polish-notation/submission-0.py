class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = set()
        for o in ['+','-','/','*']:
            operands.add(o)
        
        stack = []
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                continue
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(b+a)
            elif token == '-':
                stack.append(b-a)
            elif token == '*':
                stack.append(b*a)
            else:
                stack.append(int(b/a))
        return stack[0]        