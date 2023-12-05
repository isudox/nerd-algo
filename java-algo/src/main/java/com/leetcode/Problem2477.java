package com.leetcode;

import java.util.*;

/**
 * 2477. Minimum Fuel Cost to Report to the Capital
 * https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital
 */
public class Problem2477 {
    private long ans = 0L;

    public long minimumFuelCost(int[][] roads, int seats) {
        int n = roads.length;
        List<Integer>[] g = new List[n + 1];
        for (int i = 0; i <= n; i++) {
            g[i] = new ArrayList<Integer>();
        }
        for (int[] e : roads) {
            g[e[0]].add(e[1]);
            g[e[1]].add(e[0]);
        }
        dfs(0, -1, seats, g);
        return ans;
    }

    private int dfs(int cur, int pre, int seats, List<Integer>[] g) {
        int peopleSum = 1;
        for (int nxt : g[cur]) {
            if (nxt != pre) {
                int peopleCnt = dfs(nxt, cur, seats, g);
                peopleSum += peopleCnt;
                ans += (peopleCnt + seats - 1) / seats;
            }
        }
        return peopleSum;
    }
}
