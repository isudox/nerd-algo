package com.leetcode;

/**
 * 2698. Find the Punishment Number of an Integer
 */
public class Problem2698 {
    public int punishmentNumber(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (dfs(Integer.toString(i * i), 0, i)) {
                ans += i * i;
            }
        }
        return ans;
    }

    public boolean dfs(String s, int pos, int target) {
        if (pos == s.length()) {
            return target == 0;
        }
        int cur = 0;
        for (int i = pos; i < s.length(); i++) {
            cur = cur * 10 + s.charAt(i) - '0';
            if (cur > target) {
                break;
            }
            if (dfs(s, i + 1, target - cur)) {
                return true;
            }
        }
        return false;
    }
}
