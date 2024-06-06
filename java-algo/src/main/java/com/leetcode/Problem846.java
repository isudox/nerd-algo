package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 846. Hand of Straights
 * https://leetcode.com/problems/hand-of-straights/
 */
public class Problem846 {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length;
        if (n % groupSize > 0) {
            return false;
        }
        if (groupSize == 1) {
            return true;
        }
        Map<Integer, Integer> cnts = new HashMap<>();
        int lo = hand[0], hi = hand[0];
        for (int num : hand) {
            lo = Math.min(lo, num);
            hi = Math.max(hi, num);
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }
        int start = lo;
        while (start <= hi) {
            for (int i = 0; i < groupSize; i++) {
                int cnt = cnts.getOrDefault(start + i, 0);
                if (cnt == 0) {
                    return false;
                }
                cnts.put(start + i, cnt - 1);
            }
            while (start <= hi && cnts.getOrDefault(start, 0) == 0) {
                start++;
            }
        }
        return true;
    }
}
