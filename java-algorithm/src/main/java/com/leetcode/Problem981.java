package com.leetcode;

import java.util.*;

/**
 * 981. Time Based Key-Value Store
 * https://leetcode.com/problems/time-based-key-value-store/
 */
public class Problem981 {

    private static class TimeMap {
        Map<String, List<Integer>> times;
        Map<String, String> values;

        public TimeMap() {
            this.times = new HashMap<>();
            this.values = new HashMap<>();
        }

        public void set(String key, String value, int timestamp) {
            if (!times.containsKey(key)) {
                times.put(key, new ArrayList<>());
            }
            List<Integer> list = times.get(key);
            list.add(timestamp);
            times.put(key, list);
            values.put(key + timestamp, value);
        }

        public String get(String key, int timestamp) {
            if (!times.containsKey(key)) {
                return "";
            }
            if (timestamp < times.get(key).get(0)) {
                return "";
            }
            int pos = binarySearch(times.get(key), timestamp);
            return values.get(key + times.get(key).get(pos));
        }

        // find first index of nums, which nums[index] <= target
        int binarySearch(List<Integer> nums, int target) {
            int lo = 0, hi = nums.size() - 1;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                int num = nums.get(mid);
                if (num == target) {
                    return mid;
                }
                if (num < target) {
                    if (nums.get(mid + 1) > target) {
                        return mid;
                    }
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            return lo;
        }
    }
}
