class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_c = 0
        c = 0
        for i in nums:
            if i == 0:
                if c > max_c:
                    max_c = c
                c = 0
            elif i == 1:
                c += 1
        if c > max_c:
            return c
        elif max_c > c:
            return max_c
        else:
            return max_c