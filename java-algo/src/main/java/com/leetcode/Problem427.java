package com.leetcode;

/**
 * 427. Construct Quad Tree
 * https://leetcode.com/problems/construct-quad-tree/
 */
public class Problem427 {
    public Node construct(int[][] grid) {
        if (grid == null) {
            return null;
        }
        return helper(grid, 0, 0, grid.length - 1, grid.length - 1);
    }

    private Node helper(int[][] grid, int a, int b, int c, int d) {
        if (a == c) {
            return new Node(grid[a][b] == 1, true);
        }
        int x = grid[a][b];
        boolean isLeaf = true;
        for (int i = a; i <= c; i++) {
            for (int j = b; j <= d; j++) {
                if (grid[i][j] != x) {
                    isLeaf = false;
                    break;
                }
            }
        }
        if (isLeaf) {
            return new Node(x == 1, true);
        }
        Node root = new Node(true, false);
        root.topLeft = helper(grid, a, b, a + (c - a) / 2, b + (d - b) / 2);
        root.topRight = helper(grid, a, b + (d - b) / 2 + 1, a + (c - a) / 2, d);
        root.bottomLeft = helper(grid, a + (c - a) / 2 + 1, b, c, b + (d - b) / 2);
        root.bottomRight = helper(grid, a + (c - a) / 2 + 1, b + (d - b) / 2 + 1, c, d);
        return root;
    }

    public static void main(String[] args) {
        Problem427 p = new Problem427();
        int[][] grid = new int[][]{
                {0, 1},
                {1, 0}
        };
        Node ret = p.construct(grid);
        System.out.println(ret);
    }

    private static class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;


        public Node() {
            this.val = false;
            this.isLeaf = false;
            this.topLeft = null;
            this.topRight = null;
            this.bottomLeft = null;
            this.bottomRight = null;
        }

        public Node(boolean val, boolean isLeaf) {
            this.val = val;
            this.isLeaf = isLeaf;
            this.topLeft = null;
            this.topRight = null;
            this.bottomLeft = null;
            this.bottomRight = null;
        }

        public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
            this.val = val;
            this.isLeaf = isLeaf;
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomLeft = bottomLeft;
            this.bottomRight = bottomRight;
        }
    }
}
