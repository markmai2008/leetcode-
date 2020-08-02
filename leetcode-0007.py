class Solution:
    def reverse(self, x: int) -> int:
        b = str(abs(x))
        c = b[::-1]
        d = int(c) if x > 0 else -int(c)
        if d < -2**31 or d > 2**31-1:
            return 0
        return d


if __name__ == "__main__":
    """测试代码
    """
    inputs = [1, -3, 123, 321, -123, 1234567890, 15342365969, -15342365969]
    outputs = [1, -3, 321, 123, -321, 987654321, 0, 0]

    print(list(zip(inputs, outputs)))

    solution = Solution()

    for case, (i, o) in enumerate(zip(inputs, outputs)):
        result = solution.reverse(i)
        print(f'#Case: {case+1}')
        print(f'input: {i}')
        print(f'your output: {result}')
        print(f'expected output: {o}')
        print('result: ' + ('Correct' if result == o else 'Incorrect'))
        print()
