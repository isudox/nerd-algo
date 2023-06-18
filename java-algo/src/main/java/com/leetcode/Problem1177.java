package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem1177 {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        List<Boolean> ans = new ArrayList<>();
        int[] count = new int[s.length() + 1];
        for (int i = 0; i < s.length(); i++) {
            count[i + 1] = count[i] ^ (1 << (s.charAt(i) - 'a'));
        }
        for (int[] q : queries) {
            int l = q[0], r = q[1], k = q[2];
            int bit = 0, x = count[r + 1] ^ count[l];
            while (x > 0) {
                x &= x - 1;
                bit++;
            }
            ans.add(bit <= k * 2 + 1);
        }
        return ans;
    }
}
