from typing import List


class Solution:
    def containsDuplicateTLE(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i == j:
                    continue
                if b == a:
                    return True
        return False

    def containsDuplicateSET(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        lst = sorted(nums)
        n = len(nums)
        for i in range(1, n):
            if lst[i] == lst[i - 1]:
                return True
        return False


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([7, 2, 6, 1], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        (list(range(10000, 0, -1)), False),
        ([], False),
        ([1, 2, 3, 4, 5], False)
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.containsDuplicate(i)
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
