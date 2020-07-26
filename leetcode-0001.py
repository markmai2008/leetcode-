class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i, num in enumerate(nums):
            #print('i = ', i, num)
            for j, num2 in enumerate (nums):
                #print('  j = ', j, num2)
                if num+num2==target and i!=j:
                    print(i, j, num+num2)
                    return [i,j]
        
if __name__ == '__main__':
    solution = Solution()
    num = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(num, target))
