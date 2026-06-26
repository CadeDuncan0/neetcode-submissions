class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # convert array to map
        map = {}
        for i, val in enumerate(nums):
            missingNum = target-val
            missingIdx = map.get(missingNum, -1)

            if missingIdx != -1 and missingIdx != i:
                return [map[target-val], i]
            
            map[val] = i

        
        