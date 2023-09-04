package com.leetcode;

import com.common.TreeNode;

/**
 * 449. Serialize and Deserialize BST
 * https://leetcode.com/problems/serialize-and-deserialize-bst/
 */
public class Problem449 {
    private static class Codec {
        public String serialize(TreeNode root) {
            if (root == null) {
                return "";
            }
            StringBuilder sb = new StringBuilder();
            sb.append(root.val);
            if (root.left != null) sb.append(",").append(serialize(root.left));
            if (root.right != null) sb.append(",").append(serialize(root.right));
            return sb.toString();
        }

        public TreeNode deserialize(String data) {
            if (data.length() == 0) {
                return null;
            }
            String[] arr = data.split(",");
            int[] nums = new int[arr.length];
            for (int i = 0; i < arr.length; i++) {
                nums[i] = Integer.parseInt(arr[i]);
            }
            return helper(nums, 0, nums.length - 1);
        }

        private TreeNode helper(int[] nums, int start, int end) {
            if (nums.length == 0 || end < start) {
                return null;
            }
            TreeNode root = new TreeNode(nums[start]);
            int pos = start + 1;
            while (pos < nums.length && nums[pos] < nums[start]) {
                pos++;
            }
            root.left = helper(nums, start + 1, pos - 1);
            root.right = helper(nums, pos, end);
            return root;
        }
    }
}
