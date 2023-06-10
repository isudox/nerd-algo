package com.leetcode;

/**
 * 1170. Compare Strings by Frequency of the Smallest Character
 * https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
 */
public class Problem1170 {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        int[] store = new int[2001];
        for (String w : words) {
            int cnt = helper(w);
            store[cnt] += 1;
        }
        for (int i = 1; i < store.length; i++) {
            store[i] += store[i - 1];
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int cnt = helper(queries[i]);
            ans[i] = store[2000] - store[cnt];
        }
        return ans;
    }

    private int helper(String q) {
        int[] cnt = new int[26];
        for (int i = 0; i < q.length(); i++) {
            cnt[q.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) {
                return cnt[i];
            }
        }
        return 0;
    }
}
