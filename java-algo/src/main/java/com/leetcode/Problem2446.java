package com.leetcode;

public class Problem2446 {
    public boolean haveConflict(String[] event1, String[] event2) {
        int[] startTime1 = parse(event1[0]), endTime1 = parse(event1[1]);
        int[] startTime2 = parse(event2[0]), endTime2 = parse(event2[1]);
        int startH1 = startTime1[0], startM1 = startTime1[1], endH1 = endTime1[0], endM1 = endTime1[1];
        int startH2 = startTime2[0], startM2 = startTime2[1], endH2 = endTime2[0], endM2 = endTime2[1];
        return !((startH1 > endH2 || (startH1 == endH2 && startM1 > endM2)) || (startH2 > endH1 || (startH2 == endH1 && startM2 > endM1)));
    }

    private int[] parse(String time) {
        String[] seg = time.split(":");
        int h = Integer.parseInt(seg[0]), m = Integer.parseInt(seg[1]);
        return new int[]{h, m};
    }
}
