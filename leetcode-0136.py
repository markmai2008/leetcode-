from typing import List


class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        """ 基础解法：整体单次遍历，比较一个数前后是否都不一样 """
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(-1, n - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]

    def singleNumber2(self, nums: List[int]) -> int:
        """ 优化1：只遍历偶数下标的数字，找出第一个与其后边的数字不相等的即为结果 """
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(0, n - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

    def singleNumber3(self, nums: List[int]) -> int:
        """ 优化2：通过集合维护未配对的元素 """
        s = set()
        for a in nums:
            if a in s:
                s.remove(a)
            else:
                s.add(a)
        return s.pop()

    def singleNumber(self, nums: List[int]) -> int:
        """ 优化3：将所有数字进行异或运算 """
        a = 0
        for b in nums:
            a ^= b
        return a

if __name__ == "__main__":
    """测试代码
    """

    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([1, 1, 2, 3, 3], 2),
        ([1, 1, 2], 2),
        (list(range(10000, 0, -1))+list(range(10000, 1, -1)), 1),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.singleNumber(i)
            correct = result == o
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的输出: {repr(result)}')
        print('结果: ' + ('正确' if correct else '错误'))
        print()

    print('测试结果:', all_result)
    yes_count = sum([1 if x == '.' else 0 for x in all_result])
    no_count = sum([1 if x == 'x' else 0 for x in all_result])
    print(
        f'共测试 {len(all_result)} 个样例，'
        f'成功 {yes_count} 个，'
        f'失败 {no_count} 个'
    )
    if 'x' in all_result:
        print('测试失败，请检查你的代码！')
    else:
        print('测试通过，所有的测试数据均返回了正确的答案！')
