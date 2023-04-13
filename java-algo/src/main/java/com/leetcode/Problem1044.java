package com.leetcode;

import java.util.HashSet;
import java.util.Set;

public class Problem1044 {
    public String longestDupSubstring(String s) {
        int i = 1, j = s.length();
        String ans = "";
        while (i < j) {
            int mid = i + (j - i) / 2;
            Tuple t = isDup(s, mid);
            if (t.flag) {
                ans = t.str;
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        return ans;
    }

    private Tuple isDup(String s, int x) {
        Set<String> seen = new HashSet<>();
        for (int i = 0; i <= s.length() - x; i++) {
            String subStr = s.substring(i, i + x);
            if (seen.contains(subStr)) {
                return new Tuple(true, subStr);
            }
            seen.add(subStr);
        }
        return new Tuple(false, "");
    }

    static class Tuple {
        boolean flag;
        String str;

        public Tuple(boolean flag, String str) {
            this.flag = flag;
            this.str = str;
        }
    }
}
