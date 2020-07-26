class Solution:
    def binary_search(self, nums, target):
        ''' 要写的内容填在这里
        >>> 做完这道题之后，尝试解决 leetcode 题目：
        https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/

        提示：
        1. 先顺序枚举第一个数，时间复杂度为 O(N)
        2. 然后用二分查找的办法在剩余的数组里面查找 target 减去第一个数的结果，
        时间复杂度为 O(log(N))

        这样综合的时间复杂度为 O(N * log(N))，优于暴力算法 O(N * N)
        '''
        n = len(nums)

        l = -1
        r = n
        while l < r -1:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i,a in enumerate (numbers):
            b = target - a
            k = self.binary_search(numbers[i+1:], b)
            j = i+k+1
            if j < n and numbers[j] == b:
                return(i+1,j+1)


        