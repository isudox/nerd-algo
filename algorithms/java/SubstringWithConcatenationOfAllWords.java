public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<Integer>();
        if (words.length == 0)
            return result;
        List<String> wordList = Arrays.asList(words);
        int len = words[0].length();
        int sLen = s.length();
        if (len > sLen)
            return result;
        int wordsLen = len * (words.length);
        int i = 0;
        while (i <= sLen - wordsLen) {
            String word = s.substring(i, i + len);
            if (wordList.contains(word)) {
                String substr = s.substring(i, i + wordsLen);
                if (isValid(substr, wordList, len))
                    result.add(i);
            }
            i++;
        }
        return result;
    }

    private boolean isValid(String str, List<String> wordList, int len) {
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < str.length() / len; i++) {
            String s = str.substring(i * len, (i + 1) * len);
            list.add(s);
        }
        for (String s : wordList) {
            if (list.contains(s)) {
                list.remove(s);
            } else {
                return false;
            }
        }
        return true;
    }
}
