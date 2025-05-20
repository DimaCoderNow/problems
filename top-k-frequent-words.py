class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = {}
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
        return [i[0] for i in sorted(freqs.items(), key=lambda x: (-x[1], x[0]))[:k]]
