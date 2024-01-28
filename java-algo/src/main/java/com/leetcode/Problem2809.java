package com.leetcode;

import java.util.*;

public class Problem2809 {
    public int minimumTime(List<Integer> nums1, List<Integer> nums2, int x) {
        int n = nums1.size(), s1 = 0, s2 = 0;
        int[] dp = new int[n + 1];
        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int a = nums1.get(i), b = nums2.get(i);
            list.add(Arrays.asList(b, a));
            s1 += a;
            s2 += b;
        }
        list.sort(Comparator.comparingInt(a -> a.get(0)));
        for (int i = 1; i <= n; i++) {
            int b = list.get(i - 1).get(0), a = list.get(i - 1).get(1);
            for (int j = i; j > 0; j--) {
                dp[j] = Math.max(dp[j], dp[j - 1] + j * b + a);
            }
        }
        for (int i = 0; i <= n; i++) {
            if (s2 * i + s1 - dp[i] <= x) {
                return i;
            }
        }
        return -1;
    }
}
