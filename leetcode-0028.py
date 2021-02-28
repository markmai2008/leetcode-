class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            # 判断偏移i个位置是否重合
            yes = True
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    yes = False
                    break
            if yes:
                return i
        return -1


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (('hello', 'll'), 2),
        (('aaaa', 'bba'), -1),
        (('aaaa', 'aaaaaa'), -1),
        (('aaaa', ''), 0),
        (('', 'bba'), -1),
        (('', ''), 0),
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
            result = solution.strStr(*i)
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
