from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 双指针解法 """
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        ans = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 暴力双层循环，O(m*n) """
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        k = 0
        ans = []
        for i in range(m):
            for j in range(k, n):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    k = j + 1
                    break
        return ans

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 改善了内层循环，提前跳出，但最坏情况依然是O(n*m) """
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        k = 0
        ans = []
        for i in range(m):
            for j in range(k, n):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    k = j + 1
                    break
                if nums2[j] > nums1[i]:
                    break
        return ans

    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 改善了内层循环，忽略了nums2中较小的元素，循环部分可以达到O(m+n) """
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        k = 0
        ans = []
        for i in range(m):
            for j in range(k, n):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    k = j + 1
                    break
                elif nums2[j] > nums1[i]:
                    break
                else:
                    k = j + 1
        return ans


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([1, 2, 2, 1], [2, 2]), [2, 2]),
        (([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
        (([61, 24, 20, 58, 95, 53, 17, 32, 45, 85, 70, 20, 83, 62, 35, 89, 5, 95, 12, 86, 58, 77, 30, 64, 46, 13, 5, 92, 67, 40, 20, 38, 31, 18, 89, 85, 7, 30, 67, 34, 62, 35, 47, 98, 3, 41, 53, 26, 66, 40, 54, 44, 57, 46, 70, 60, 4, 63, 82, 42, 65, 59, 17, 98, 29, 72, 1, 96, 82, 66, 98, 6, 92, 31, 43, 81, 88, 60, 10, 55, 66, 82, 0, 79, 11, 81],
          [5, 25, 4, 39, 57, 49, 93, 79, 7, 8, 49, 89, 2, 7, 73, 88, 45, 15, 34, 92, 84, 38, 85, 34, 16, 6, 99, 0, 2, 36, 68, 52, 73, 50, 77, 44, 61, 48]), [5, 4, 57, 79, 7, 89, 88, 45, 34, 92, 38, 85, 6, 0, 77, 44, 61]),
        (([1, 2, 2, 4, 5], [1, 1, 2, 3, 4]), [1, 2, 4]),
        (([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [1, 2, 3, 4, 5, 6, 7, 8]), []),
        # (([9]*100000, [1]*100000), []),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.intersect(*i)
            correct = sorted(result) == sorted(o)
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
