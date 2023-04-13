package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 821. Shortest Distance to a Character
 * https://leetcode.com/problems/shortest-distance-to-a-character/
 */
public class Problem821 {
    public int[] shortestToChar(String s, char c) {
        int[] ans = new int[s.length()];
        List<Integer> store = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                store.add(i);
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                continue;
            }
            int pos = search(store, i);
            int x = Math.abs(store.get(pos % store.size()) - i);
            int y = Math.abs(store.get((pos + 1) % store.size()) - i);
            int z = Math.abs(store.get((pos - 1 + store.size()) % store.size()) - i);
            ans[i] = Math.min(Math.min(x, y), z);
        }
        return ans;
    }

    private int search(List<Integer> nums, int target) {
        int lo = 0, hi = nums.size() - 1, mid;
        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (nums.get(mid) == target) {
                return mid;
            }
            if (nums.get(mid) < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
