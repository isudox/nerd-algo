package com.leetcode;

/**
 * 307. Range Sum Query - Mutable
 * https://leetcode.com/problems/range-sum-query-mutable/
 */
public class Problem307 {
    private static class NumArray {
        int[] tree;
        int n;
        int[] nums;

        int lowbit(int x) {
            return x & -x;
        }

        int query(int x) {
            int ret = 0;
            for (int i = x; i > 0; i -= lowbit(i)) {
                ret += tree[i];
            }
            return ret;
        }

        void add(int x, int v) {
            for (int i = x; i <= n; i += lowbit(i)) {
                tree[i] += v;
            }
        }
        public NumArray(int[] nums) {
            this.nums = nums;
            this.n = nums.length;
            tree = new int[n + 1];
            for (int i = 0; i < n; i++) {
                add(i + 1, nums[i]);
            }
        }

        public void update(int index, int val) {
            add(index + 1, val - nums[index]);
            nums[index] = val;
        }

        public int sumRange(int left, int right) {
            return query(right + 1) - query(left);
        }
    }
}
