package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 508. Most Frequent Subtree Sum
 * https://leetcode.com/problems/most-frequent-subtree-sum/
 */
public class Problem508 {
    private final Map<Integer, Integer> counter = new HashMap<>();

    public int[] findFrequentTreeSum(TreeNode root) {
        dfs(root);
        int max = 0;
        List<Integer> ans = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            if (entry.getValue() == max) {
                ans.add(entry.getKey());
            } else if (entry.getValue() > max) {
                max = entry.getValue();
                ans.clear();
                ans.add(entry.getKey());
            }
        }
        int[] arr = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            arr[i] = ans.get(i);
        }
        return arr;
    }

    private int dfs(TreeNode node) {
        if (node.left == null && node.right == null) {
            int cnt = counter.getOrDefault(node.val, 0);
            counter.put(node.val, cnt + 1);
            return node.val;
        }
        int sum = node.val;
        if (node.left != null) {
            sum += dfs(node.left);
        }
        if (node.right != null) {
            sum += dfs(node.right);
        }
        int cnt = counter.getOrDefault(sum, 0);
        counter.put(sum, cnt + 1);
        return sum;
    }
}
