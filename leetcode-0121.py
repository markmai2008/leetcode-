from typing import List


class Solution:
    def maxProfitTLE(self, prices: List[int]) -> int:
        y = 0
        for i, c in enumerate(prices):
            for d in prices[i + 1:]:
                if d - c > y:
                    y = d - c
        return y

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        y = 0
        x = prices[0]
        for c in prices:
            if c < x:
                x = c
            if c - x > y:
                y = c - x
        return y


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([7, 2, 6, 1], 4),
        ([1, 1, 1, 1, 1, 1], 0),
        (list(range(10000, 0, -1))+[0]*16000+[1, 2, 3], 3),
        ([], 0)
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.maxProfit(i)
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
