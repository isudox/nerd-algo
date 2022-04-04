package com.leetcode;

/**
 * 410. Split Array Largest Sum
 * https://leetcode-cn.com/problems/split-array-largest-sum/
 */
public class Problem410 {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        int avg = preSum[n] % m == 0 ? preSum[n] / m : preSum[n] / m + 1;
        int ans = 0;
        int[] segments = new int[m];
        for (int i = 0; i < m; i++) {
            int cur = avg * i;
            int pos = search(preSum, cur);
            int seg = preSum[pos];
            ans = Math.max(ans, seg);
        }
        return ans;
    }

    private int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1, mid;
        while (i < j) {
            if (i + 1 == j) {
                break;
            }
            mid = i + (j - i) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                i = mid;
            } else {
                j = mid;
            }
        }
        return i;
    }

    public static void main(String[] args) {
        Problem410 p = new Problem410();
        System.out.println(p.splitArray(new int[]{1, 2, 3, 4, 5}, 2));
    }
}