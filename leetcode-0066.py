from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        for a in digits:
            x = x * 10
            x += a
        x += 1
        ans = []
        while x != 0:
            ans.append(x % 10)
            x = x // 10
        return ans[::-1]


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([1, 2, 3],), [1, 2, 4]),
        (([4, 3, 2, 1],), [4, 3, 2, 2]),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.plusOne(*i)
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
