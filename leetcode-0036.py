from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            if x.count(".") + len(set(x+['.'])) != 10:
                return False
        for x in zip(*board):
            if x.count(".") + len(set(x+('.',))) != 10:
                return False
        for a in (0, 3, 6):
            for b in (0, 3, 6):
                x = board[a][b:b+3]+board[a+1][b:b+3]+board[a+2][b:b+3]
                if x.count(".") + len(set(x+['.'])) != 10:
                    return False
        return True

    def isValidSudoku3(self, board: List[List[str]]) -> bool:
        for x in board:
            if "." in x and x.count(".") + len(set(x)) != 10 or \
                    "." not in x and len(set(x)) != 9:
                return False
        for x in zip(*board):
            if "." in x and x.count(".") + len(set(x)) != 10 or \
                    "." not in x and len(set(x)) != 9:
                return False
        for a in (0, 3, 6):
            for b in (0, 3, 6):
                x = board[a][b:b+3]+board[a+1][b:b+3]+board[a+2][b:b+3]
                if "." in x and x.count(".") + len(set(x)) != 10 or \
                        "." not in x and len(set(x)) != 9:
                    return False
        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        """ 这里会出现一种反例，判重时如果没有.条件会将对的情况判错 """
        for x in board:
            if x.count(".") + len(set(x)) != 10:
                return False
        for x in zip(*board):
            if x.count(".") + len(set(x)) != 10:
                return False
        for a in (0, 3, 6):
            for b in (0, 3, 6):
                x = board[a][b:b+3]+board[a+1][b:b+3]+board[a+2][b:b+3]
                if x.count(".") + len(set(x)) != 10:
                    return False
        return True


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]],), True),
        (([["1", "2", "3", "4", "5", "6", "7", "8", "9"],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "."]],), True),
    ]
    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.isValidSudoku(*i)
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
