package com.leetcode;

import com.common.Pair;
import com.common.TreeNode;

import java.util.*;

/**
 * 2096. Step-By-Step Directions From a Binary Tree Node to Another
 * https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
 */
class Problem2096{
    public String getDirections(TreeNode root, int startValue, int destValue) {
        Map<Integer, TreeNode> parentMap = new HashMap<>();
        TreeNode startNode = findStartNode(root, startValue);
        populateParentMap(root, parentMap);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(startNode);
        Set<TreeNode> visitedNodes = new HashSet<>();
        Map<TreeNode, Pair<TreeNode, String>> pathTracker = new HashMap<>();
        visitedNodes.add(startNode);
        while (!queue.isEmpty()) {
            TreeNode currentNode = queue.poll();
            if (currentNode.val == destValue) {
                return backtrackPath(currentNode, pathTracker);
            }
            if (parentMap.containsKey(currentNode.val)) {
                TreeNode parentNode = parentMap.get(currentNode.val);
                if (!visitedNodes.contains(parentNode)) {
                    queue.add(parentNode);
                    pathTracker.put(parentNode, new Pair<>(currentNode, "U"));
                    visitedNodes.add(parentNode);
                }
            }
            if (currentNode.left != null && !visitedNodes.contains(currentNode.left)) {
                queue.add(currentNode.left);
                pathTracker.put(currentNode.left, new Pair<>(currentNode, "L"));
                visitedNodes.add(currentNode.left);
            }
            if (currentNode.right != null && !visitedNodes.contains(currentNode.right)) {
                queue.add(currentNode.right);
                pathTracker.put(currentNode.right, new Pair<>(currentNode, "R"));
                visitedNodes.add(currentNode.right);
            }
        }
        return "";
    }

    private String backtrackPath(TreeNode node, Map<TreeNode, Pair<TreeNode, String>> pathTracker) {
        StringBuilder path = new StringBuilder();
        while (pathTracker.containsKey(node)) {
            path.append(pathTracker.get(node).getSecond());
            node = pathTracker.get(node).getFirst();
        }
        path.reverse();
        return path.toString();
    }

    private void populateParentMap(TreeNode node, Map<Integer, TreeNode> parentMap) {
        if (node == null) {
            return;
        }
        if (node.left != null) {
            parentMap.put(node.left.val, node);
            populateParentMap(node.left, parentMap);
        }
        if (node.right != null) {
            parentMap.put(node.right.val, node);
            populateParentMap(node.right, parentMap);
        }
    }

    private TreeNode findStartNode(TreeNode node, int startValue) {
        if (node == null) {
            return null;
        }
        if (node.val == startValue) {
            return node;
        }
        TreeNode leftResult = findStartNode(node.left, startValue);
        if (leftResult != null) {
            return leftResult;
        }
        return findStartNode(node.right, startValue);
    }
}
