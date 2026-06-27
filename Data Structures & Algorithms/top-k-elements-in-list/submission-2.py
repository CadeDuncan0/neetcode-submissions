class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outputList = []
        frequencyCounts = {}

        for n in nums:
            frequencyCounts[n] = frequencyCounts.get(n, 0) + 1
            
        # Get list of keys sorted by their values in the dictionary
        sorted_elements = sorted(frequencyCounts.keys(), key=lambda x: frequencyCounts[x], reverse=True)
        top_k = sorted_elements[:k]

        return top_k