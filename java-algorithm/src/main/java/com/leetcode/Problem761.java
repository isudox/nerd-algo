package com.leetcode;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * 761. Special Binary String
 * https://leetcode.cn/problems/special-binary-string
 */
class Problem761 {
    public String makeLargestSpecial(String s) {
        int n = s.length();
        if (n <= 2) return s;
        int cnt = 0, left = 0;
        List<String> subs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                cnt++;
                continue;
            }
            if (--cnt == 0) {
                subs.add("1" + makeLargestSpecial(s.substring(left + 1, i)) + "0");
                left = i + 1;
            }
        }
        subs.sort(Comparator.reverseOrder());
        return String.join("", subs);
    }
}
