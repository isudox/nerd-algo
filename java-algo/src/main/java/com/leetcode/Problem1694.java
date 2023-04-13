package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1694. Reformat Phone Number
 * https://leetcode.com/problems/reformat-phone-number/
 */
public class Problem1694 {
    public String reformatNumber(String number) {
        List<Character> list = new ArrayList<>();
        for (int i = 0; i < number.length(); i++) {
            char ch = number.charAt(i);
            if (ch != ' ' && ch != '-') {
                list.add(ch);
            }
        }
        List<String> segments = new ArrayList<>();
        int i = 0;
        while (i < list.size() - 4) {
            StringBuilder cur = new StringBuilder();
            for (int j = i; j < i + 3; j++) {
                cur.append(list.get(j));
            }
            segments.add(cur.toString());
            i += 3;
        }
        if (list.size() - i == 4) {
            for (int j = i; j < list.size(); j += 2) {
                StringBuilder str = new StringBuilder();
                for (int k = j; k < j + 2; k++) {
                    str.append(list.get(k));
                }
                segments.add(str.toString());
            }
        } else {
            StringBuilder str = new StringBuilder();
            for (int j = i; j < list.size(); j++) {
                str.append(list.get(j));
            }
            segments.add(str.toString());
        }
        return String.join("-", segments);
    }
}
