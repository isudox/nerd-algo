package com.leetcode;

import java.util.*;

/**
 * 710. Random Pick with Blacklist
 * https://leetcode.com/problems/random-pick-with-blacklist/
 */
public class Problem710 {
    List<int[]> list = new ArrayList<>();
    int[] sum = new int[100010];
    int size;
    Random random = new Random();

    public Problem710(int n, int[] blacklist) {
        Arrays.sort(blacklist);
        int m = blacklist.length;
        if (m == 0) {
            list.add(new int[]{0, n - 1});
        } else {
            if (blacklist[0] != 0) {
                list.add(new int[]{0, blacklist[0] - 1});
            }
            for (int i = 1; i < m; i++) {
                if (blacklist[i - 1] == blacklist[i] - 1) {
                    continue;
                }
                list.add(new int[]{blacklist[i - 1] + 1, blacklist[i] - 1});
            }
            if (blacklist[m - 1] != n - 1) {
                list.add(new int[]{blacklist[m - 1] + 1, n - 1});
            }
        }
        size = list.size();
        for (int i = 1; i <= size; i++) {
            int[] info = list.get(i - 1);
            sum[i] = sum[i - 1] + info[1] - info[0] + 1;
        }
    }

    public int pick() {
        int x = random.nextInt(sum[size]) + 1;
        int left = 1, right = size;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (sum[mid] >= x) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        int[] info = list.get(right - 1);
        return info[1] - (sum[right] - x);
    }
}
