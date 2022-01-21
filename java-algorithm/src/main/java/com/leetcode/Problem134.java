package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 134. Gas Station
 * https://leetcode.com/problems/gas-station/
 */
public class Problem134 {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        if (n == 1) {
            return gas[0] >= cost[0] ? 0 : -1;
        }
        int total = 0, neg = 0;
        List<Integer> candidates = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            gas[i] -= cost[i];
            total += gas[i];
            if (gas[i] > 0) {
                candidates.add(i);
            } else if (gas[i] < 0) {
                neg += gas[i];
            }
        }
        if (total < 0) return -1;
        for (int i : candidates) {
            if (check(neg, gas, i)) {
                return i;
            }
        }
        return -1;
    }

    private boolean check(int neg, int[] earn, int stop) {
        int cur = 0;
        int cnt = 0;
        while (cur >= 0) {
            cur += earn[stop];
            cnt++;
            if (cnt == earn.length || cur + neg >= 0) {
                return true;
            }
            stop++;
            if (stop == earn.length) {
                stop = 0;
            }
        }
        return false;
    }
}
