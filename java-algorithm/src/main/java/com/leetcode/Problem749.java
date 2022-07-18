package com.leetcode;

import java.util.*;

/**
 * 749. Contain Virus
 * https://leetcode.com/problems/contain-virus
 */
public class Problem749 {
    private int[][] grid;
    private int m;
    private int n;
    private int ans;
    private int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int containVirus(int[][] isInfected) {
        this.grid = isInfected;
        this.m = isInfected.length;
        this.n = isInfected[0].length;
        while (true) {
            int cnt = getCnt();
            if (cnt == 0) {
                break;
            }
            ans += cnt;
        }
        return ans;
    }

    private int getCnt() {
        boolean[][] visited = new boolean[m][n];
        int max = 0, ans = 0;
        List<Set<Integer>> l1 = new ArrayList<>();
        List<Set<Integer>> l2 = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    Set<Integer> s1 = new HashSet<>();
                    Set<Integer> s2 = new HashSet<>();
                    int b = search(i, j, s1, s2, visited);
                    int a = s2.size();
                    if (a > max) {
                        max = a;
                        ans = b;
                    }
                    l1.add(s1);
                    l2.add(s2);
                }
            }
        }
        for (int i = 0; i < l2.size(); i++) {
            for (int loc : l2.get(i).size() == max ? l1.get(i) : l2.get(i)) {
                int x = loc / n, y = loc % n;
                grid[x][y] = l2.get(i).size() == max ? -1 : 1;
            }
        }
        return ans;
    }

    private int search(int r, int c, Set<Integer> s1, Set<Integer> s2, boolean[][] visited) {
        int ans = 0;
        Deque<int[]> q = new ArrayDeque<>();
        visited[r][c] = true;
        q.addLast(new int[]{r, c});
        s1.add(r * n + c);
        while (!q.isEmpty()) {
            int[] key = q.pollFirst();
            int x = key[0], y = key[1];
            for (int[] dir : dirs) {
                int nx = x + dir[0], ny = y + dir[1], loc = nx * n + ny;
                if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny]) {
                    if (grid[nx][ny] == 1) {
                        s1.add(loc);
                        visited[nx][ny] = true;
                        q.addLast(new int[]{nx, ny});
                    } else if (grid[nx][ny] == 0) {
                        s2.add(loc);
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
}
