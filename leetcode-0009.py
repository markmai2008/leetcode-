class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

        
if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (0, True),
        (1, True),
        (-1, False),
        (123, False),
        (121, True),
        (-121, False),
        (10, False),
        (123454321, True),
        (12345678987654321, True),
    ]


    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        result = solution.isPalindrome(i)
        correct = result == o
        all_result += '.' if correct else 'x'
        print(f'#Case: {case+1}')
        print(f'input: {i}')
        print(f'your output: {result}')
        print(f'expected output: {o}')
        print('result: ' + ('Correct' if correct else 'Incorrect'))
        print()
    
    print('Test result:', all_result)

    
