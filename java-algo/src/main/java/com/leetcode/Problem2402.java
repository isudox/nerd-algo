package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * 2402. Meeting Rooms III
 * https://leetcode.com/problems/meeting-rooms-iii/
 */
public class Problem2402 {
    public int mostBooked(int n, int[][] meetings) {
        int sz = meetings.length;
        int[] oriTimes = new int[sz];
        int[] durations = new int[sz];
        for (int i = 0; i < sz; i++) {
            oriTimes[i] = meetings[i][0];
            durations[i] = meetings[i][1] - meetings[i][0];
        }
        Arrays.sort(meetings, Comparator.comparingInt(o -> o[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        var meetingCnt = new int[n];
        var usedRooms = new PriorityQueue<>((Comparator<int[]>) (a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });
        var unusedRooms = new PriorityQueue<Integer>();
        for (int i = 0; i < n; i++) {
            unusedRooms.offer(i);
        }
        Arrays.sort(meetings, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        for (int[] meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            while (!usedRooms.isEmpty() && usedRooms.peek()[0] <= start) {
                int room = usedRooms.poll()[1];
                unusedRooms.offer(room);
            }
            if (!unusedRooms.isEmpty()) {
                int room = unusedRooms.poll();
                usedRooms.offer(new int[]{end, room});
                meetingCnt[room]++;
            } else {
                int roomReleaseTime = usedRooms.peek()[0];
                int room = usedRooms.poll()[1];
                usedRooms.offer(new int[]{roomReleaseTime + end - start, room});
                meetingCnt[room]++;
            }
        }
        int maxCnt = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            if (meetingCnt[i] > maxCnt) {
                maxCnt = meetingCnt[i];
                ans = i;
            }
        }
        return ans;
    }
}
