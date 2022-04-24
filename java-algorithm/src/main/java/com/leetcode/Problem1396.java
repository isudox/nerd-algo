package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1396. Design Underground System
 * https://leetcode.com/problems/design-underground-system/
 */
public class Problem1396 {
    private static class UndergroundSystem {

        private final Map<Integer, Tuple> checkInMap = new HashMap<>();  // id -> (startStation, startTime)
        private final Map<String, int[]> routeMap = new HashMap<>();

        public UndergroundSystem() {
        }

        public void checkIn(int id, String stationName, int t) {
            checkInMap.put(id, new Tuple(stationName, t));
        }

        public void checkOut(int id, String stationName, int t) {
            Tuple checkIn = checkInMap.get(id);
            checkInMap.remove(id);
            String key = checkIn.getStartStation() + "_" + stationName;
            int time = t - checkIn.getStartTime();
            int[] count = routeMap.getOrDefault(key, new int[2]);
            count[0] += time;
            count[1]++;
            routeMap.put(key, count);
        }

        public double getAverageTime(String startStation, String endStation) {
            String key = startStation + "_" + endStation;
            int[] count = routeMap.get(key);
            return 1.0 * count[0] / count[1];
        }

        private static class Tuple {
            private int startTime;
            private String startStation;

            public Tuple(String station, int time) {
                this.startStation = station;
                this.startTime = time;
            }

            public int getStartTime() {
                return startTime;
            }

            public String getStartStation() {
                return startStation;
            }
        }
    }
}
