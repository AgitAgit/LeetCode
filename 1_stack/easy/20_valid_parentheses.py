class Solution:
    def isValid(self, s: str) -> bool:
        stack_1 = []
        # Perhaps one stack, and whenever there is a match of closed
        # Brackets you pop the pair off.
        # If there stack is empty at the end, return true.
        # stack_2 = []
        # stack_3 = []
        for i in s:
            if stack_1:
                a = stack_1[len(stack_1) - 1]
                if a == '(':
                    if i == ')':
                        stack_1.pop()
                        continue
                if a == '{':
                    if i == '}':
                        stack_1.pop()
                        continue
                if a == '[':
                    if i == ']':
                        stack_1.pop()
                        continue
            stack_1.append(i)
        
        if stack_1 == []:
            return True
        return False