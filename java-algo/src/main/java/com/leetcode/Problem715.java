package com.leetcode;


import java.util.Map;
import java.util.TreeMap;

/**
 * Range  Module
 * https://leetcode.com/problems/range-module
 */
public class Problem715 {
    private static class RangeModule {
        TreeMap<Integer, Integer> intervals;
    
        public RangeModule() {
            intervals = new TreeMap<Integer, Integer>();
        }
    
        public void addRange(int left, int right) {
            Map.Entry<Integer, Integer> entry = intervals.higherEntry(left);
            if (entry != intervals.firstEntry()) {
                Map.Entry<Integer, Integer> start = entry != null ? intervals.lowerEntry(entry.getKey()) : intervals.lastEntry();
                if (start != null && start.getValue() >= right) {
                    return;
                }
                if (start != null && start.getValue() >= left) {
                    left = start.getKey();
                    intervals.remove(start.getKey());
                }
            }
            while (entry != null && entry.getKey() <= right) {
                right = Math.max(right, entry.getValue());
                intervals.remove(entry.getKey());
                entry = intervals.higherEntry(entry.getKey());
            }
            intervals.put(left, right);
        }
    
        public boolean queryRange(int left, int right) {
            Map.Entry<Integer, Integer> entry = intervals.higherEntry(left);
            if (entry == intervals.firstEntry()) {
                return false;
            }
            entry = entry != null ? intervals.lowerEntry(entry.getKey()) : intervals.lastEntry();
            return entry != null && right <= entry.getValue();
        }
    
        public void removeRange(int left, int right) {
            Map.Entry<Integer, Integer> entry = intervals.higherEntry(left);
            if (entry != intervals.firstEntry()) {
                Map.Entry<Integer, Integer> start = entry != null ? intervals.lowerEntry(entry.getKey()) : intervals.lastEntry();
                if (start != null && start.getValue() >= right) {
                    int ri = start.getValue();
                    if (start.getKey() == left) {
                        intervals.remove(start.getKey());
                    } else {
                        intervals.put(start.getKey(), left);
                    }
                    if (right != ri) {
                        intervals.put(right, ri);
                    }
                    return;
                } else if (start != null && start.getValue() > left) {
                    intervals.put(start.getKey(), left);
                }
            }
            while (entry != null && entry.getKey() < right) {
                if (entry.getValue() <= right) {
                    intervals.remove(entry.getKey());
                    entry = intervals.higherEntry(entry.getKey());
                } else {
                    intervals.put(right, entry.getValue());
                    intervals.remove(entry.getKey());
                    break;
                }
            }
        }
    }
}

