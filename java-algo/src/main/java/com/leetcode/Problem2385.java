package com.leetcode;

import com.common.TreeNode;

import java.util.*;

/**
 * 2385. Amount of Time for Binary Tree to Be Infected
 * https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
 */
public class Problem2385 {
    public int amountOfTime(TreeNode root, int start) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        recur(root, null, graph);
        int ans = -1;
        Set<Integer> removed = new HashSet<>();
        Deque<Integer> q = new ArrayDeque<>();
        q.offerLast(start);
        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                int val = q.pollFirst();
                removed.add(val);
                for (int sib : graph.get(val)) {
                    if (!removed.contains(sib)) {
                        q.offerLast(sib);
                    }
                }
            }
            ans++;
        }
        return ans;
    }

    private void recur(TreeNode cur, TreeNode pre, Map<Integer, Set<Integer>> graph) {
        if (cur == null) {
            return;
        }
        graph.put(cur.val, new HashSet<>());
        if (pre != null) {
            graph.get(pre.val).add(cur.val);
            graph.get(cur.val).add(pre.val);
        }
        recur(cur.left, cur, graph);
        recur(cur.right, cur, graph);
    }
}
