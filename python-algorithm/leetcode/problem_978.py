"""978. Longest Turbulent Subarray
https://leetcode.com/problems/longest-turbulent-subarray/

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each
adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:

  Input: [9,4,2,10,7,8,8,1,9]
  Output: 5
  Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

Example 2:

  Input: [4,8,12,16]
  Output: 2

Example 3:

  Input: [100]
  Output: 1

Note:

  1 <= A.length <= 40000
  0 <= A[i] <= 10^9
"""
from typing import List


class Solution:

    def max_turbulence_size(self, a: 'List[int]') -> 'int':
        size, max_count, start = len(a), 1, 0
        for i in range(1, size):
            c = (a[i - 1] > a[i]) - (a[i - 1] < a[i])
            if c == 0:
                start = i
            elif i == size - 1 \
                or c * ((a[i] > a[i + 1]) - (a[i] < a[i + 1])) != -1:
                max_count = max(max_count, i - start + 1)
                start = i
        return max_count

    def max_turbulence_size_2(self, arr: 'List[int]') -> 'int':
        def get_start(index: int) -> int:
            while index + 1 < n and arr[index] == arr[index + 1]:
                index += 1
            return index

        n = len(arr)
        ans = 1
        i = get_start(0)
        j = i + 1
        if j == n:
            return 1
        flag = arr[j] - arr[i] > 0
        while j < n:
            if j == n - 1:
                ans = max(ans, j - i + 1)
                break
            elif (flag and arr[j + 1] < arr[j]) or (not flag and arr[j + 1] > arr[j]):
                j += 1
                flag = not flag
            else:
                ans = max(ans, j - i + 1)
                i = get_start(j)
                j = i + 1
                if j == n:
                    break
                flag = arr[j] - arr[i] > 0
        return ans

    def max_turbulence_size_time_limit(self, a: 'List[int]') -> 'int':
        """
        Non-Acceptable Approach, Time Limit Exceeded
        """
        size = len(a)
        if size < 2:
            return size
        if size == 2:
            return 1 if a[0] == a[1] else 2
        i, max_count = 0, 1
        while i < size - 1:
            if a[i] == a[i + 1]:
                i += 1
                continue
            pre_type = True if a[i] > a[i + 1] else False
            temp_count = 2
            max_count = max(max_count, temp_count)
            j = i + 1
            while j < size - 1:
                if a[j] == a[j + 1]:
                    break
                cur_type = a[j] > a[j + 1]
                if pre_type == cur_type:
                    break
                else:
                    temp_count += 1
                    max_count = max(max_count, temp_count)
                    pre_type = cur_type
                j += 1
            i += 1
        return max_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.max_turbulence_size_2([1, 5, 3]))
