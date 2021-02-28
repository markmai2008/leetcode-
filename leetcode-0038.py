class Solution:
    def nextStr(self, s):
        ans = ''
        a = 1
        b = s[0]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += f'{a}{b}'
                a = 1
                b = s[i]
            else:
                a += 1
        ans += f'{a}{b}'
        return ans

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.nextStr(self.countAndSay(n-1))


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        ((1,), '1'),
        ((2,), '11'),
        ((3,), '21'),
        ((4,), '1211'),
        ((5,), '111221'),
        #((30,), '11'),
    ]
    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: ')
        print(i)
        print(f'正确答案:')
        print(o)
        try:
            result = solution.countAndSay(*i)
            correct = result == o
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的答案: ')
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
