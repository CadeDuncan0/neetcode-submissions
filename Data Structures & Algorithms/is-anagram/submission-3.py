class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countmapS = {}
        countmapT = {}

        # string must be same length
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                countmapS[s[i]] = countmapS.get(s[i], 0) + 1
                countmapT[t[i]] = countmapT.get(t[i], 0) + 1

        return countmapS == countmapT