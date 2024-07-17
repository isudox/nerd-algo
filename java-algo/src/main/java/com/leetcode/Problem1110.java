package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 1110. Delete Nodes And Return Forest
 * https://leetcode.com/problems/delete-nodes-and-return-forest/
 */
public class Problem1110 {
    Set<Integer> toDeleted = new HashSet<>();
    List<TreeNode> ans = new ArrayList<>();

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        if (root == null) {
            return ans;
        }
        for (int d : to_delete) {
            toDeleted.add(d);
        }
        dfs(root, null, -1);
        return ans;
    }

    private void dfs(TreeNode cur, TreeNode par, int dir) {
        if (cur == null) {
            return;
        }
        if (toDeleted.isEmpty() && par != null) {
            return;
        }
        if (toDeleted.contains(cur.val)) {
            toDeleted.remove(cur.val);
            dfs(cur.left, null, -1);
            dfs(cur.right, null, -1);
            if (par != null) {
                if (dir == 0) {
                    par.left = null;
                } else {
                    par.right = null;
                }
            }
            return;
        }
        if (par == null) {
            ans.add(cur);
        }
        dfs(cur.left, cur, 0);
        dfs(cur.right, cur, 1);
    }
}
