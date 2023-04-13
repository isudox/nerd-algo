package com.leetcode;

/**
 * 2156. Find Substring With Given Hash Value
 * https://leetcode.com/problems/find-substring-with-given-hash-value/
 */
public class Problem2156 {
    public String subStrHash(String s, int power, int modulo, int k, int hashValue) {
        int n = s.length();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = s.charAt(i) - 'a' + 1;
        }
        long hash = 0;
        int start = -1;
        long mul = 1;
        for (int i = n - 1; i >= n - k; i--) {
            hash = (hash * power + arr[i]) % modulo;
            if (i != n - k) {
                mul = mul * power % modulo;
            }
        }
        if (hash == hashValue) {
            start = n - k;
        }
        for (int i = n - k - 1; i >= 0; i--) {
            hash = ((hash - arr[i + k] * mul % modulo + modulo) * power + arr[i]) % modulo;
            if (hash == hashValue) {
                start = i;
            }
        }
        return start < 0 ? "" : s.substring(start, start + k);
    }
}
