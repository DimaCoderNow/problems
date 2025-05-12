class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        return list(map(lambda x: x[0], sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:k]))
