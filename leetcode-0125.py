class Solution:
    def isPalindrome1(self, s: str) -> bool:
        a = [c.upper() for c in s if c.isalnum()]
        return a == a[::-1]

    def isPalindrome(self, s: str) -> bool:
        a = [c.upper() for c in s if c.isalnum()]
        n = len(a)
        for i in range(n // 2):
            j = - i - 1
            if a[i] != a[j]:
                return False
        return True


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (('A man, a plan, a canal: Panama',), True),
        (('race a car',), False),
    ]
    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: ')
        print(i)
        print(f'期望输出:')
        print(o)
        try:
            result = solution.isPalindrome(*i)
            correct = result == o
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的输出: ')
        print(result)
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
