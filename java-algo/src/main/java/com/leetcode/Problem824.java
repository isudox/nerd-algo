package com.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 824. Goat Latin
 * https://leetcode.com/problems/goat-latin/
 * 如果单词以元音开头（'a', 'e', 'i', 'o', 'u'），在单词后添加"ma"。
 * 例如，单词 "apple" 变为 "applema" 。
 * 如果单词以辅音字母开头（即，非元音字母），移除第一个字符并将它放到末尾，之后再添加"ma"。
 * 例如，单词 "goat" 变为 "oatgma" 。
 * 根据单词在句子中的索引，在单词最后添加与索引相同数量的字母'a'，索引从 1 开始。
 * 例如，在第一个单词后添加 "a" ，在第二个单词后添加 "aa" ，以此类推。
 */
public class Problem824 {
    private static final Set<Character> vowels = new HashSet<>();

    static {
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');
    }

    public String toGoatLatin(String sentence) {
        String[] words = sentence.split(" ");
        List<String> list = new ArrayList<>();
        StringBuilder suffix = new StringBuilder();
        for (String word : words) {
            if (word.length() == 0) {
                continue;
            }
            suffix.append("a");
            String tmp;
            if (vowels.contains(word.charAt(0))) {
                tmp = word + "ma" + suffix;
            } else {
                tmp = word.substring(1) + word.charAt(0) + "ma" + suffix;
            }
            list.add(tmp);
        }
        return String.join(" ", list);
    }
}
