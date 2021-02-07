class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        a = True
        if s == '':
            return 0
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            s = s[1:]
            a = False
        x = 0
        for c in s:
            if not c.isdigit():
                break
            x *= 10
            x += int(c)
        if not a:
            x = -x
        if x < -2 ** 31:
            return -2 ** 31
        if x > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return x


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (('42',), 42),
        (('-42',), -42),
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
            result = solution.myAtoi(*i)
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
