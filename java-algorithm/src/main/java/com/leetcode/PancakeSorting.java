package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 969. Pancake Sorting
 * https://leetcode.com/problems/pancake-sorting/
 * <p>
 * Given an array A, we can perform a pancake flip: We choose some positive
 * integer k <= A.length, then reverse the order of the first k elements of A.
 * We want to perform zero or more pancake flips (doing them one after another
 * in succession) to sort the array A.
 * <p>
 * Return the k-values corresponding to a sequence of pancake flips that sort A.
 * Any valid answer that sorts the array within 10 * A.length flips will be
 * judged as correct.
 * <p>
 * Example 1:
 * <p>
 * Input: [3,2,4,1]
 * Output: [4,2,4,3]
 * Explanation:
 * We perform 4 pancake flips, with k values 4, 2, 4, and 3.
 * Starting state: A = [3, 2, 4, 1]
 * After 1st flip (k=4): A = [1, 4, 2, 3]
 * After 2nd flip (k=2): A = [4, 1, 2, 3]
 * After 3rd flip (k=4): A = [3, 2, 1, 4]
 * After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
 * <p>
 * Example 2:
 * <p>
 * Input: [1,2,3]
 * Output: []
 * Explanation: The input is already sorted, so there is no need to flip anything.
 * Note that other answers, such as [3, 3], would also be accepted.
 * <p>
 * Note:
 * <p>
 * 1 <= A.length <= 100
 * A[i] is a permutation of [1, 2, ..., A.length]
 */
public class PancakeSorting {

    public List<Integer> pancakeSort(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        int size = nums.length;

        for (int i = size; i > 0; i--) {
            int index = findMax(nums, i);
            if (index != i - 1) {
                if (index == 0) {
                    reverse(nums, i);
                    ans.add(i);
                } else {
                    reverse(nums, index + 1);
                    reverse(nums, i);
                    ans.add(index + 1);
                    ans.add(i);
                }
            }
        }

        return ans;
    }

    private static int findMax(int[] nums, int n) {
        int index = 0;
        for (int i = 0; i < n; i++) {
            index = nums[i] > nums[index] ? i : index;
        }
        return index;
    }

    private static void reverse(int[] nums, int n) {
        int temp;
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
