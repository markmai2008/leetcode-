from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs)
        t = strs[0]
        a = len(strs[0])
        for s in strs:
            if len(s) < a:
                a = len(s)
                t = s
        for k in range(a):
            for i, s in enumerate(strs):
                if s[k] != strs[0][k]:
                    return s[:k]
        return t


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (["flower", "flow", "flight"], 'fl'),
        (["dog", "racecar", "car"], ''),
        (["flower", "flow", "fl"], 'fl'),
        (["flower", "flow", ""], ''),
        ([], ''),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.longestCommonPrefix(i)
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
