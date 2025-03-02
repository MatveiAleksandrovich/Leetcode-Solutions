# 150. Evaluate Reverse Polish Notation


class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                res = self.perform_operation(a, b, i)
                stack.append(res)
        
        return int(stack[-1])
    
    def perform_operation(self, a, b, operand):
        a = int(a)
        b = int(b)
        if operand == '+':
            return a + b
        elif operand == '-':
            return a - b
        elif operand == '/':
            return a / b
        else:
            return a * b
