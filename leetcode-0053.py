from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        def mx(l=0, r=n):
            m = (l + r) // 2
            if l == r -1:
                return nums[l]
            # 计算中间合并的最大子序列和
            result = 0 # TODO: 未实现
            
            if l < m:
                result = max(result, mx(l, m))
            if m < r:
                result = max(result, mx(m, r))

        return mx()

    def maxSubArrayAccumulateTLE(self, nums: List[int]) -> int:
        """ 暴力算法优化，通过累加数组 O(N) 预处理，将求和操作复杂度降到 O(1)
        整体时间复杂度降到 O(N^2)，超时 """
        n = len(nums)
        a = nums[0]
        # 预处理累加列表
        acc = [0]
        for x in nums:
            acc.append(acc[-1] + x)
        # print(acc)
        # 执行求最大值
        for i in range(n):
            for j in range(i, n):
                b = acc[j + 1] - acc[i]
                if b > a:
                    a = b
        return a

    def maxSubArrayBruteForceTLE(self, nums: List[int]) -> int:
        """ 暴力算法 O(N^3)，超时 """
        n = len(nums)
        a = nums[0]
        for i in range(n):
            for j in range(i, n):
                b = sum(nums[i:j+1])
                if b > a:
                    a = b
        return a


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([50, 50, 50, -1000, 100, -100], 150),
        ([0, 0, 0, 0, 0, 0], 0),
        ([-1, -1, -1, -1], -1),
        ([-1, -2, -3, -4, -5, -6], -1),
        ([-99999999, -99999999], -99999999),
        ([1], 1),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.maxSubArray(i)
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
