package com.leetcode;

import java.util.*;

/**
 * 855. Exam Room
 * https://leetcode.com/problems/exam-room/
 */
public class Problem855 {
    static class ExamRoom {
        private final int n;
        private final TreeSet<Integer> seats;

        public ExamRoom(int n) {
            this.n = n;
            this.seats = new TreeSet<>();
        }

        public int seat() {
            if (seats.isEmpty()) {
                seats.add(0);
                return 0;
            }
            int left = seats.first(), d = left, pos = 0;
            for (int seat : seats) {
                int tmp = (seat - left) / 2;
                if (tmp > d) {
                    d = tmp;
                    pos = left + d;
                }
                left = seat;
            }
            if (n - 1 - seats.last() > d) {
                pos = n - 1;
            }
            seats.add(pos);
            return pos;
        }

        public void leave(int p) {
            this.seats.remove(p);
        }
    }
}
