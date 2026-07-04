class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we are finding the length * height output value
        # which means find the furthest length of indices while keeping height as high as possible
        leftI = 0
        rightI = len(heights) - 1

        leftHeight = 0
        rightHeight = 0

        output = 0
        while leftI != rightI:
            leftHeight = heights[leftI]
            rightHeight = heights[rightI]
            length = rightI - leftI
            
            output = max(output, min(leftHeight, rightHeight) * length)
            if leftHeight < rightHeight:
                leftI += 1
            else:
                rightI -= 1
            
        return output

        