package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem844 {
    public boolean backspaceCompare(String s, String t) {
        return helper(s).equals(helper(t));
    }

    private String helper(String input) {
        List<Character> characters = new ArrayList<>();
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '#') {
                if (characters.size() > 0) {
                    characters.remove(characters.size() - 1);
                }
            } else {
                characters.add(input.charAt(i));
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : characters) {
            sb.append(ch);
        }
        return sb.toString();
    }
}
