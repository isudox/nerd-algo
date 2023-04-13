package com.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 649. Dota2 Senate
 * https://leetcode.com/problems/dota2-senate/
 */
public class Problem649 {

    public String predictPartyVictory(String senate) {
        int n = senate.length();
        boolean[] disabled = new boolean[n];
        List<Integer> dires = new ArrayList<>(), radiants = new ArrayList<>();
        for (int i = 0; i < n; i++)
            (senate.charAt(i) == 'R' ? radiants : dires).add(i);
        while (true) {
            for (int i = 0; i < n; i++) {
                if (disabled[i]) continue;
                disable(senate.charAt(i) == 'R' ? dires : radiants, i, disabled);
                if (dires.size() == 0) return "Radiant";
                if (radiants.size() == 0) return "Dire";
            }
        }
    }

    private void disable(List<Integer> list, int start, boolean[] disabled) {
        int idx = Math.abs(Collections.binarySearch(list, start) + 1);
        for (int i = idx; i < list.size(); i++) {
            int pos = list.get(i);
            if (!disabled[pos]) {
                disabled[pos] = true;
                list.remove(i);
                return;
            }
        }
        for (int i = 0; i < idx; i++) {
            int pos = list.get(i);
            if (!disabled[pos]) {
                disabled[pos] = true;
                list.remove(i);
                return;
            }
        }
    }
}
