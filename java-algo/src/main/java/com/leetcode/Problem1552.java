package com.leetcode;

import java.util.Arrays;

/**
 * 1552. Magnetic Force Between Two Balls
 * https://leetcode.com/problems/magnetic-force-between-two-balls/
 */
public class Problem1552 {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int n = position.length;
        int lo = 1, hi = position[n - 1] - position[0];
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (check(position, m, mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }

    private boolean check(int[] position, int m, int interval) {
        int cnt = 1, i = 1, pre = position[0];
        while (cnt < m && i < position.length) {
            while (i < position.length && position[i] - pre < interval) {
                i++;
            }
            if (i == position.length) {
                return false;
            }
            pre = position[i];
            i++;
            cnt++;
        }
        return cnt >= m;
    }
}
