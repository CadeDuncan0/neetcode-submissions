class Solution:
    def checkValidString(self, s: str) -> bool:
        # store all '*' locations

        # store a stack of '('
        leftStack = []
        rightStack = []
        stars = []

        for i in range(len(s)):
            if s[i] == '*':
                stars.append(i)

            elif s[i] == '(':
                leftStack.append(i)
            
            elif leftStack and s[i] == ')':
                leftStack.pop()
            elif stars:
                stars.pop()
            else: 
                rightStack.append(i)

        while stars:
            if leftStack and stars[-1] > leftStack[-1]:
                leftStack.pop()
            elif rightStack and stars[-1] < rightStack[-1]:
                rightStack.pop()
                
            stars.pop()

        return not stars and not leftStack and not rightStack
        