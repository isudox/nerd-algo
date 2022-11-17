package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 792. Number of Matching Subsequences
 * https://leetcode.com/problems/number-of-matching-subsequences/
 */
public class Problem792 {
    public int numMatchingSubseq(String s, String[] words) {
        Map<Character, List<Integer>> store = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            List<Integer> list = store.getOrDefault(s.charAt(i), new ArrayList<>());
            list.add(i);
            store.put(s.charAt(i), list);
        }
        int ans = 0;
        for (String word : words) {
            int preIndex = -1;
            boolean ok = true;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (!store.containsKey(c)) {
                    ok = false;
                    break;
                }
                List<Integer> list = store.get(c);
                preIndex = getIndex(list, preIndex);
                if (preIndex == -1) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ans++;
            }
        }
        return ans;
    }

    private int getIndex(List<Integer> list, int num) {
        int lo = 0, hi = list.size() - 1;
        if (list.get(hi) <= num) {
            return -1;
        }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int tmp = list.get(mid);
            if (tmp <= num) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return list.get(lo);
    }
}
