package com.leetcode;

import com.common.TreeNode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 2196. Create Binary Tree From Descriptions
 * https://leetcode.com/problems/create-binary-tree-from-descriptions/
 */
public class Problem2196 {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> map = new HashMap<>();
        Set<Integer> children = new HashSet<>();
        for (int[] desc : descriptions) {
            int par = desc[0], child = desc[1], left = desc[2];
            if (!map.containsKey(par)) {
                map.put(par, new TreeNode(par));
            }
            if (!map.containsKey(child)) {
                map.put(child, new TreeNode(child));
            }
            TreeNode parNode = map.get(par), childNode = map.get(child);
            if (left == 1) {
                parNode.left = childNode;
            } else {
                parNode.right = childNode;
            }
            children.add(child);
        }
        for (int node : map.keySet()) {
            if (!children.contains(node)) {
                return map.get(node);
            }
        }
        return null;
    }
}
