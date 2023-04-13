package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 112. Path Sum
 * https://leetcode.com/problems/path-sum/
 *
 * Given a binary tree and a sum, determine if the tree has a root-to-leaf path
 * such that adding up all the values along the path equals the given sum.
 *
 * Note: A leaf is a node with no children.
 *
 * Example:
 *
 * Given the below binary tree and sum = 22,
 *
 *       5
 *      / \
 *     4   8
 *    /   / \
 *   11  13  4
 *  /  \      \
 * 7    2      1
 * return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
 */
public class Problem112 {

	/**
	 * Recursive
     * Time complexity: O(N)
	 * Space complexity: O(H), H is the height of tree.
	 */
    public boolean hasPathSum(TreeNode root, int sum) {
		if (null == root)
			return false;
		if (null == root.left && null == root.right)
			return sum == root.val;
		if (null != root.left && hasPathSum(root.left, sum - root.val))
			return true;
		if (null != root.right && hasPathSum(root.right, sum - root.val))
			return true;
		return false;
    }

	public boolean hasPathSum2(TreeNode root, int targetSum) {
		if (root == null) {
			return false;
		}
		Deque<Tuple> queue = new ArrayDeque<>();
		queue.offerLast(new Tuple(root, targetSum));
		while (!queue.isEmpty()) {
			int n = queue.size();
			for (int i = 0; i < n; i++) {
				Tuple t = queue.pollFirst();
				TreeNode node = t.node;
				int target = t.target;
				if (t.valid()) {
					return true;
				}
				if (t.node.left != null) {
					queue.offerLast(new Tuple(t.node.left, t.target - t.node.val));
				}
				if (t.node.right != null) {
					queue.offerLast(new Tuple(t.node.right, t.target - t.node.val));
				}
			}
		}
		return false;
	}

	private static class Tuple {
		TreeNode node;
		int target;

		public Tuple(TreeNode node, int target) {
			this.node = node;
			this.target = target;
		}

		public boolean valid() {
			return node.left == null && node.right == null && node.val == target;
		}
	}
}
