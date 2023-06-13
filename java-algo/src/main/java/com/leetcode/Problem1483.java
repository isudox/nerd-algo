package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem1483 {
    static class TreeAncestor {

        BiLinkNode[] nodes;

        public TreeAncestor(int n, int[] parent) {
            nodes = new BiLinkNode[n];
            for (int i = 0; i < n; i++) {
                nodes[i] = new BiLinkNode(i);
            }
            for (int i = 0; i < n; i++) {
                if (parent[i] == -1) {
                    continue;
                }
                nodes[parent[i]].children.add(nodes[i]);
                nodes[i].parent = nodes[parent[i]];
            }
        }

        public int getKthAncestor(int node, int k) {
            BiLinkNode cur = nodes[node];
            for (int i = 0; i < k; i++) {
                if (cur.parent == null) {
                    return -1;
                }
                cur = cur.parent;
            }
            return cur == null ? -1 : cur.val;
        }
    }

    static class BiLinkNode {
        int val;
        BiLinkNode parent;
        List<BiLinkNode> children;

        public BiLinkNode(int val) {
            this.val = val;
            this.children = new ArrayList<>();
        }
    }

}
