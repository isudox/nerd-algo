package com.leetcode;

public class MinimumAreaRectangle2 {

    public double minAreaFreeRect(int[][] points) {
        int len = points.length;
        if (len < 4)
            return 0.0D;
        double ans = Double.MAX_VALUE;
        for (int i = 0; i < len - 3; i++)
            for (int j = i + 1; j < len - 2; j++)
                for (int k = j + 1; k < len - 1; k++)
                    for (int l = k + 1; l < len; l++)
                        if (is_rect(points[i], points[j], points[k], points[l]))
                            ans = Math.min(ans, rect_area(points[i], points[j], points[k], points[l]));

        return ans < Double.MAX_VALUE ? ans : 0.0D;
    }

    private double dist(double[] a, int[] b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }

    private boolean is_rect(int[] a, int[] b, int[] c, int[] d) {
        double center_x = (a[0] + b[0] + c[0] + d[0]) * 0.25D;
        double center_y = (a[1] + b[1] + c[1] + d[1]) * 0.25D;
        double[] center = {center_x, center_y};
        return dist(center, a) == dist(center, b) && dist(center, b) == dist(center, c) && dist(center, c) == dist(center, d);
    }

    private double triangle_area(int[] p1, int[] p2, int[] p3) {
        return 0.5D * Math.abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] -
                p1[0] * p3[1] - p2[0] * p1[1] - p3[0] * p2[1]);
    }

    private double rect_area(int[] p1, int[] p2, int[] p3, int[] p4) {
        return triangle_area(p1, p2, p3) + triangle_area(p2, p3, p4);
    }
}
