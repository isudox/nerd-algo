package com.leetcode;

public class Problem705 {
    private static class MyHashSet {

        private final int[] nums = new int[1000001];

        public MyHashSet() {
        }

        public void add(int key) {
            nums[key] = 1;
        }

        public void remove(int key) {
            nums[key] = 0;
        }

        public boolean contains(int key) {
            return nums[key] == 1;
        }
    }
}
