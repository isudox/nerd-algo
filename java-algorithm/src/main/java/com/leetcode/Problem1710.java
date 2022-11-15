package com.leetcode;

import java.util.Arrays;

/**
 * 1710. Maximum Units on a Truck
 * https://leetcode.com/problems/maximum-units-on-a-truck/
 */
public class Problem1710 {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        int ans = 0;
        int i = 0;
        while (truckSize > 0 && i < boxTypes.length) {
            int n = Math.min(truckSize, boxTypes[i][0]);
            ans += n * boxTypes[i][1];
            truckSize -= n;
            i++;
        }
        return ans;
    }
}
