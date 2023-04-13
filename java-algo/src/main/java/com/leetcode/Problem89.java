package com.leetcode;

import java.util.*;

/**
 * 89. Gray Code
 * https://leetcode.com/problems/gray-code/
 *
 * 1 <= n <= 16
 */
public class Problem89 {
    public List<Integer> grayCode(int n) {
        if (n == 0)
            return Collections.singletonList(0);
        int size = (int) Math.pow(2, n);
        boolean[] visited = new boolean[size];
        List<Integer> ans = new ArrayList<>(size);
        ans.add(0);
        visited[0] = true;
        dfs(0, visited, n, ans);
        return ans;
    }

    private void dfs(int num, boolean[] visited, int n, List<Integer> store) {
        int nextNum = getNext(num, visited, n);
        if (nextNum == 0)
            return;
        store.add(nextNum);
        dfs(nextNum, visited, n, store);
    }

    private int getNext(int num, boolean[] visited, int n) {
        for (int i = 0; i < n; i++) {
            int bit = (num >> i) & 1;
            int nextNum = bit == 0 ? num + (1 << i) : num - (1 << i);
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                return nextNum;
            }
        }
        return 0;
    }
}
