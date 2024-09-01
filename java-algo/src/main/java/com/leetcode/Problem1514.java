package com.leetcode;

/**
 * 1514. Path with Maximum Probability
 * https://leetcode.com/problems/path-with-maximum-probability
 */
public class Problem1514 {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        double[] maxProb = new double[n];
        maxProb[start] = 1d;
        for (int i = 0; i < n - 1; i++) {
            boolean hasUpdated = false;
            for (int j = 0; j < edges.length; j++) {
                int u = edges[j][0], v = edges[j][1];
                double pathProb = succProb[j];
                if (maxProb[u] * pathProb > maxProb[v]) {
                    maxProb[v] = maxProb[u] * pathProb;
                    hasUpdated = true;
                }
                if (maxProb[v] * pathProb > maxProb[u]) {
                    maxProb[u] = maxProb[v] * pathProb;
                    hasUpdated = true;
                }
            }
            if (!hasUpdated) {
                break;
            }
        }
        return maxProb[end];
    }
}
