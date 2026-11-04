class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        c_max= 0
        for i in nums:
            if i == 1:
                c += 1
            elif i == 0:
                c = 0
            if c_max <= c:
                c_max = c
        return c_max
