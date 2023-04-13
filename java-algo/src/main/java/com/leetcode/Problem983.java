package com.leetcode;

/**
 * 983. Minimum Cost For Tickets
 * https://leetcode.com/problems/minimum-cost-for-tickets/
 */
public class Problem983 {
    public int mincostTickets1(int[] days, int[] costs) {
        int[] memo = new int[days.length];
        return dfs(0, days, costs, memo);
    }

    private int dfs(int i, int[] days, int[] costs, int[] memo) {
        if (i >= days.length) {
            return 0;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        int[] d = new int[]{1, 7, 30};
        int ret = costs[2] * days.length;
        for (int x = 0; x < 3; x++) {
            int j = i;
            while (j < days.length) {
                if (days[j] - days[i] >= d[x]) {
                    break;
                }
                j++;
            }
            ret = Math.min(ret, costs[x] + dfs(j, days, costs, memo));
        }
        return memo[i] = ret;
    }

    public int mincostTickets(int[] days, int[] costs) {
        int size = days.length;
        int[][] multi = new int[size + 1][3];
        for (int i = 0; i <= size; i++) {
            multi[i] = new int[]{0, 0, 0};
        }

        for (int i = 1; i <= size; i++) {
            multi[i][0] = costs[0] + getMin(multi[i - 1]);
            int j = i;
            while (j > 0 && days[i - 1] - days[j - 1] < 7) j--;
            multi[i][1] = costs[1] + getMin(multi[j]);

            while (j > 0 && days[i - 1] - days[j - 1] < 30) j--;
            multi[i][2] = costs[2] + getMin(multi[j]);
        }

        return getMin(multi[size]);
    }

    private int getMin(int[] nums) {
        int min = nums[0];
        for (int num : nums) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }
}
