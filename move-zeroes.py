class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        a = len(nums)-1
        while a >= 0:            
            if nums[a] == 0:
                nums.append(nums.pop(a))
            a -= 1
