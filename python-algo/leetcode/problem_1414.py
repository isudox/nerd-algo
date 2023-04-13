"""1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
1, 1, 2, 3, 5, 8, 13
"""
import bisect


def find_min_fibonacci_numbers(k: int) -> int:
    nums = [1, 1]
    while nums[-1] < k:
        nums.append(nums[-1] + nums[-2])
    ans = 0
    while k > 0:
        pos = bisect.bisect_left(nums, k)
        if nums[pos] > k:
            pos -= 1
        k -= nums[pos]
        ans += 1
    return ans
