package com.leetcode;

import java.util.Random;

/**
 * 478. Generate Random Point in a Circle
 * https://leetcode.com/problems/generate-random-point-in-a-circle/
 */
public class Problem478 {
    private double max;
    private double r;
    private double x0;
    private double y0;
    private Random random;

    public Problem478(double radius, double x_center, double y_center) {
        this.max = radius * radius;
        this.r = radius;
        this.x0 = x_center;
        this.y0 = y_center;
        this.random = new Random();
    }

    public double[] randPoint() {
        while (true) {
            double x = -r + 2 * r * random.nextDouble();
            double y = -r + 2 * r * random.nextDouble();
            if (x * x + y * y <= max) {
                return new double[]{x + x0, y + y0};
            }
        }
    }
}
