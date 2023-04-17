package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1042. Flower Planting With No Adjacent
 * https://leetcode.com/problems/flower-planting-with-no-adjacent/
 */
public class Problem1042 {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] path : paths) {
            graph[path[0] - 1].add(path[1] - 1);
            graph[path[1] - 1].add(path[0] - 1);
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[5];
            for (int v : graph[i]) {
                visited[ans[v]] = true;
            }
            for (int j = 1; j < 5; j++) {
                if (!visited[j]) {
                    ans[i] = j;
                    break;
                }
            }
        }
        return ans;
    }
}
