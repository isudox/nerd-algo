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

    public int splitArray2(int[] nums, int m) {
        int lo = 0, hi = 0;
        for (int num : nums) {
            hi += num;
            if (lo < num) {
                lo = num;
            }
        }
        while (lo < hi) {
            int mid = (hi - lo) / 2 + lo;
            if (check(nums, mid, m)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean check(int[] nums, int limit, int m) {
        int sum = 0, cnt = 1;
        for (int num : nums) {
            if (sum + num > limit) {
                cnt++;
                if (cnt > m) {
                    return false;
                }
                sum = num;
            } else {
                sum += num;
            }
        }
        return cnt <= m;
    }
}
