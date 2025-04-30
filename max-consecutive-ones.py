def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    res = 0
    tmp = 0
    for i in nums:
        if i == 1:
            tmp += 1
        elif tmp > res:
            res = tmp
            tmp = 0
        else:
            tmp = 0
    return max(tmp, res)
