class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seenMap = {}

        for n in nums1:
            seenMap[n] = 1

        returnArr = set()

        for n in nums2:
            if seenMap.get(n, 0) == 1:
                returnArr.add(n)

        return list(returnArr)