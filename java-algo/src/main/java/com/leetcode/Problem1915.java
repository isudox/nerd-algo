package com.leetcode;

/**
 * 1915. Number of Wonderful Substrings
 * https://leetcode.com/problems/number-of-wonderful-substrings/
 */
public class Problem1915 {
    public long wonderfulSubstrings(String word) {
        long ans = 0;
        int[] store = new int[1024];
        store[0] = 1;
        for (int i = 0, sum = 0; i < word.length(); i++) {
            sum ^= 1 << (word.charAt(i) - 'a');
            ans += store[sum];
            for (int j = 1; j < 1024; j <<= 1) {
                ans += store[sum ^ j];
            }
            store[sum]++;
        }
        return ans;
    }
}
