class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_operation(token):
            if token in ['+', '-', '*', '/']:
                return True
            return False
        
        from collections import deque
        tokens = deque(tokens)
        stack = deque()
        while len(tokens)!=0:
            tok = tokens.popleft()
            if is_operation(tok):
                num1 = stack.pop()
                num2 = stack.pop()
                ans = str(int(eval(num2 + tok + num1)))
                stack.append(ans)
                continue
            
            stack.append(tok)
            
        return int(float(stack.pop()))

