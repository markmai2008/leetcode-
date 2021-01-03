from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        for j in range(m//2):
            n = m-j-j
            for i in range(n - 1):
                matrix[0+j][i+j], matrix[i+j][n-1+j] =\
                    matrix[i+j][n-1+j], matrix[0+j][i+j]
            for i in range(n - 1):
                matrix[1+i+j][0+j], matrix[n-1+j][1+i+j] =\
                    matrix[n-1+j][1+i+j], matrix[1+i+j][0+j]
            for i in range(n - 1):
                matrix[0+j][i+j], matrix[n-1+j][n-1-i+j] =\
                    matrix[n-1+j][n-1-i+j], matrix[0+j][i+j]


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([[1, 2, 3],
           [4, 5, 6],
            [7, 8, 9]],),
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]),
        (([[5, 1, 9, 11],
           [2, 4, 8, 10],
            [13, 3, 6, 7],
           [15, 14, 12, 16]],),
         [[15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
          [16, 7, 10, 11]]),
    ]
    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: ')
        for x in i[0]:
            print(x)
        print(f'期望输出:')
        for x in o:
            print(x)
        try:
            solution.rotate(*i)
            result = i[0]
            correct = result == o
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的输出: ')
        for x in result:
            print(x)
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
