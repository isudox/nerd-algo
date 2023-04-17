package com.leetcode;

class Problem2409 {
    private static int[] month = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] arriveA = helper(arriveAlice), leaveA = helper(leaveAlice);
        int[] arriveB = helper(arriveBob), leaveB = helper(leaveBob);
        if (leaveA[0] < arriveB[0] || arriveA[0] > leaveB[0]) {
            return 0;
        }
        if (leaveA[0] == arriveB[0] && leaveA[1] < arriveB[1]) {
            return 0;
        }
        if (leaveB[0] == arriveA[0] && leaveB[1] < arriveA[1]) {
            return 0;
        }
        int ans = 0;
        int startMonth, startDay, endMonth, endDay;
        startMonth = Math.max(arriveA[0], arriveB[0]);
        endMonth = Math.min(leaveA[0], leaveB[0]);
        if (arriveA[0] > arriveB[0]) {
            startDay = arriveA[1];
        } else if (arriveB[0] > arriveA[0]) {
            startDay = arriveB[1];
        } else {
            startDay = Math.max(arriveA[1], arriveB[1]);
        }
        if (leaveA[0] < leaveB[0]) {
            endDay = leaveA[1];
        } else if (leaveA[0] > leaveB[0]) {
            endDay = leaveB[1];
        } else {
            endDay = Math.min(leaveA[1], leaveB[1]);
        }
        if (startMonth == endMonth) {
            return endDay - startDay + 1;
        }
        for (int i = startMonth + 1; i < endMonth; i++) {
            ans += month[i - 1];
        }
        return ans + month[startMonth - 1] - startDay + 1 + endDay;
    }

    private int[] helper(String date) {
        String[] dateStr = date.split("-");
        return new int[]{Integer.parseInt(dateStr[0]), Integer.parseInt(dateStr[1])};
    }
}
