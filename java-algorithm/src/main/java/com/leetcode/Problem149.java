package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 149. Max Points on a Line
 * https://leetcode.com/problems/max-points-on-a-line/
 */
public class Problem149 {
    public int maxPoints(int[][] points) {
        if (points.length < 3)
            return points.length;
        List<int[]> visited = new ArrayList<>();
        int ans = 0;
        for (int i = 0; i < points.length; i++) {
            if (ans >= points.length - i || ans > points.length / 2)
                break;
            for (int j = i + 1; j < points.length; j++) {
                ans = Math.max(ans, helper(points, i, j, visited));
            }
        }
        return ans;
    }

    private int helper(int[][] points, int i, int j, List<int[]> visited) {
        for (int[] line : visited) {
            int[] p1 = points[line[0]], p2 = points[line[1]];
            if ((points[i][0] - p1[0]) * (points[i][1] - p2[1])
                    == (points[i][1] - p1[1]) * (points[i][0] - p2[0])
                    &&
                    (points[j][0] - p1[0]) * (points[j][1] - p2[1])
                            == (points[j][1] - p1[1]) * (points[j][0] - p2[0])) {
                return 0;
            }
        }
        int cnt = 2;
        for (int k = 0; k < points.length; k++) {
            if (k == i || k == j) continue;
            if ((points[k][0] - points[i][0]) * (points[j][1] - points[i][1])
                    == (points[k][1] - points[i][1]) * (points[j][0] - points[i][0])) {
                cnt++;
            }
        }
        visited.add(new int[]{i, j});
        return cnt;
    }
}
