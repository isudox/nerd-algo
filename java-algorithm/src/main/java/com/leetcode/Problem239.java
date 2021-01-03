package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 239. Sliding Window Maximum
 * https://leetcode.com/problems/sliding-window-maximum/
 *
 * Given an array nums, there is a sliding window of size k which is moving
 * from the very left of the array to the very right.
 * You can only see the k numbers in the window. Each time the sliding window
 * moves right by one position. Return the max sliding window.
 *
 * Follow up:
 * Could you solve it in linear time?
 *
 * Example:
 *
 * Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
 * Output: [3,3,5,5,6,7]
 * Explanation:
 *
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 *  1 [3  -1  -3] 5  3  6  7       3
 *  1  3 [-1  -3  5] 3  6  7       5
 *  1  3  -1 [-3  5  3] 6  7       5
 *  1  3  -1  -3 [5  3  6] 7       6
 *  1  3  -1  -3  5 [3  6  7]      7
 *
 * Constraints:
 *
 *     1 <= nums.length <= 10^5
 *     -10^4 <= nums[i] <= 10^4
 *     1 <= k <= nums.length
 */
public class Problem239 {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n == 0 || k == 0) {
            return new int[0];
        }
        Deque<Integer> deque = new ArrayDeque<>();
        int maxIndex = 0;
        for (int i = 0; i < k; i++) {
            cleanDeque(deque, i, nums, k);
            deque.addLast(i);
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }
        int[] ans = new int[n - k + 1];
        ans[0] = nums[maxIndex];
        for (int i = k; i < n; i++) {
            cleanDeque(deque, i, nums, k);
            deque.addLast(i);
            ans[i - k + 1] = nums[deque.getFirst()];
        }
        return ans;
    }

    private void cleanDeque(Deque<Integer> deque, int index, int[] nums, int k) {
        if (deque.size() > 0 && deque.getFirst() == index - k) {
            deque.removeFirst();
        }
        while (deque.size() > 0 && nums[index] > nums[deque.getLast()]) {
            deque.removeLast();
        }
    }
}
