package com.leetcode;

/**
 * 307. Range Sum Query - Mutable
 * https://leetcode.com/problems/range-sum-query-mutable/
 */
public class Problem307 {
    private static class SegmentTree {
        int start;
        int end;
        SegmentTree left;
        SegmentTree right;
        int sum;

        public SegmentTree(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    private static class NumArray {
        SegmentTree root;

        public NumArray(int[] nums) {
            this.root = build(nums, 0, nums.length - 1);
        }

        private SegmentTree build(int[] nums, int start, int end) {
            if (start > end) return null;
            SegmentTree tree = new SegmentTree(start, end);
            if (start == end) tree.sum = nums[start];
            else {
                int mid = start + (end - start) / 2;
                tree.left = build(nums, start, mid);
                tree.right = build(nums, mid + 1, end);
                tree.sum = tree.left.sum + tree.right.sum;
            }
            return tree;
        }

        public void update(int index, int val) {
            update(root, index, val);
        }

        private void update(SegmentTree tree, int i, int val) {
            if (tree.start == tree.end) tree.sum = val;
            else {
                int mid = tree.start + (tree.end - tree.start) / 2;
                if (i <= mid) {
                    update(tree.left, i, val);
                } else {
                    update(tree.right, i, val);
                }
                tree.sum = tree.left.sum + tree.right.sum;
            }
        }

        public int sumRange(int left, int right) {
            return sumRange(this.root, left, right);
        }

        public int sumRange(SegmentTree tree, int left, int right) {
            if (tree.start == left && tree.end == right) return tree.sum;
            int mid = tree.start + (tree.end - tree.start) / 2;
            if (right <= mid) return sumRange(tree.left, left, right);
            if (left >= mid + 1) return sumRange(tree.right, left, right);
            return sumRange(tree.right, mid + 1, right) + sumRange(tree.left, left, mid);
        }
    }
}
