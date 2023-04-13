package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 295. Find Median from Data Stream
 * https://leetcode.com/problems/find-median-from-data-stream/
 */
public class Problem295 {
    static class MedianFinder {
        List<Integer> nums;

        public MedianFinder() {
            nums = new ArrayList<>();
        }

        public void addNum(int num) {
            int pos = find(num);
            nums.add(pos, num);
        }

        public double findMedian() {
            int n = nums.size();
            int mid = n / 2;
            int rem = n % 2;
            if (rem == 0) {
                return (nums.get(mid - 1) + nums.get(mid)) / 2.0;
            }
            return (double) nums.get(mid);
        }

        private int find(int num) {
            if (nums.size() == 0 || nums.get(0) >= num) {
                return 0;
            }
            if (nums.get(nums.size() - 1) <= num) {
                return nums.size();
            }
            int i = 0, j = nums.size() - 1;
            while (i < j) {
                int mid = (i + j) / 2;
                if (nums.get(mid) == num) {
                    return mid;
                }
                if (nums.get(mid) < num) {
                    i = mid + 1;
                } else {
                    j = mid;
                }
            }
            return i;
        }
    }
}
