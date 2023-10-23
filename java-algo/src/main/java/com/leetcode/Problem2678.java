package com.leetcode;

public class Problem2678 {
    public int countSeniors(String[] details) {
        int ans = 0;
        for (String detail : details) {
            int age = Integer.parseInt(detail.substring(11, 13));
            ans += age > 60 ? 1 : 0;
        }
        return ans;
    }
}
