class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # divide in half each time until target is reached
        # we know the list is sorted which allows us to use this method
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            #print(l, r, mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1