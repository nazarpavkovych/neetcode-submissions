class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mnozina = set(['+', '-', '*','/'])
        stack = []
        for i in tokens:
            if i in mnozina:
                op1=stack.pop()
                op2=stack.pop()
                if i =='*':
                    stack.append(op1*op2)
                if i == '+':
                    stack.append(op1+op2)
                if i == '-':
                    stack.append(op2-op1)
                if i == '/':
                    stack.append(int(op2/op1))
            else:
                stack.append(int(i))
        return stack.pop()