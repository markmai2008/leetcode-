from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        m = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                nums[m] = nums[i]
                m += 1
        return m
