package com.leetcode;

/**
 * 922. Sort Array By Parity II
 * https://leetcode.com/problems/sort-array-by-parity-ii/
 *
 * Given an array A of non-negative integers, half of the integers in A are odd,
 * and half of the integers are even.
 *
 * Sort the array so that whenever A[i] is odd, i is odd;
 * and whenever A[i] is even, i is even.
 *
 * You may return any answer array that satisfies this condition.
 *
 * Example 1:
 *
 * Input: [4,2,5,7]
 * Output: [4,5,2,7]
 * Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 *
 * Note:
 *
 *     2 <= A.length <= 20000
 *     A.length % 2 == 0
 *     0 <= A[i] <= 1000
 */
public class Problem922 {
    public int[] sortArrayByParityII(int[] nums) {
        int i = 0, j = 1, n = nums.length;
        while (i < n - 1 && j < n) {
            if (nums[i] % 2 == 0) {
                i += 2;
                continue;
            }
            if (nums[j] % 2 == 1) {
                j += 2;
                continue;
            }
            swap(nums, i, j);
            i += 2;
            j += 2;
        }
        return nums;
    }

    private void swap(int[] nums, int x, int y) {
        nums[x] = nums[x] ^ nums[y]; // x now becomes 15 (1111)
        nums[y] = nums[x] ^ nums[y]; // y becomes 10 (1010)
        nums[x] = nums[x] ^ nums[y]; // x becomes 5 (0101)
    }
}
