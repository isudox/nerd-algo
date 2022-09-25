package com.leetcode;

import java.util.*;
/**
 * 788. Rotated Digits
 * https://leetcode.com/problems/rotated-digits/
 */
class Problem788 {
    private Set<Integer> aSet = new HashSet<>(Arrays.asList(0, 1, 8));
    private Set<Integer> bSet = new HashSet<>(Arrays.asList(2, 5, 6, 9));

    public int rotatedDigits(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (check(i))
                ans++;
        }
        return ans;
    }

    private boolean check(int num) {
        boolean flag = false;
        while (num > 0) {
            int rem = num % 10;
            if (!aSet.contains(rem) && !bSet.contains(rem)) 
                return false;
            if (bSet.contains(rem)) 
                flag = true;
            num /= 10;
        }
        return flag;
    }
}
