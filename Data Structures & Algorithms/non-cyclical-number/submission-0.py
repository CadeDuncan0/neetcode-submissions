class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers = {}
        
        while n != 1 and seenNumbers.get(n, 0) == 0:
            result = 0
            for digit in str(n):
                result += int(digit) ** 2
            
            seenNumbers[n] = 1
            n = result

            

        return n == 1
