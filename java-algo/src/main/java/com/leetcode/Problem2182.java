package com.leetcode;

/**
 * 2182. Construct String With Repeat Limit
 */
public class Problem2182 {
    public String repeatLimitedString(String s, int repeatLimit) {
        int[] arr = new int[26];
        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'a']++;
        }
        int i = 25;
        StringBuilder ans = new StringBuilder();
        int cnt = 0;
        while (i >= 0) {
            if (arr[i] == 0) {
                i--;
                continue;
            }
            ans.append((char) ('a' + i));
            arr[i]--;
            if (arr[i] == 0) {
                cnt = 0;
                i--;
                continue;
            }
            cnt++;
            if (cnt == repeatLimit) {
                int j = i - 1;
                while (j >= 0 && arr[j] == 0) {
                    j--;
                }
                if (j < 0) {
                    break;
                }
                ans.append((char) ('a' + j));
                arr[j]--;
                cnt = 0;
            }
        }
        return ans.toString();
    }
}
