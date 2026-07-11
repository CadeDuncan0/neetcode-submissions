class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
      
        for left in range(len(s)):
            if maxLen > len(s) - left:
                return maxLen
            
            seenChars = set()
            right = left            
            
            while right < len(s) and s[right] not in seenChars:
                #print(left, s[left], right, s[right])
                seenChars.add(s[right])
                right += 1

            maxLen = max(maxLen, right - left)      
                
        return maxLen