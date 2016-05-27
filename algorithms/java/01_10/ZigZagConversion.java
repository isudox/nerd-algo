public class Solution {
    public String convert(String s, int numRows) {
        int len = s.length();
        if (len <= 2 || numRows == 1) {
            return s;
        }
        String result = "";
        int step = 2 * (numRows - 1);
        for (int currRow = 0; currRow < numRows; currRow++) {
            for (int currIndex = currRow; currIndex < len; currIndex += 2 * (numRows - 1)) {
                result += s.charAt(currIndex);
                if (currRow != 0 && currRow != numRows - 1 && currIndex + 2 * (numRows - currRow - 1) < len) {
                    result += s.charAt(currIndex + 2 * (numRows - currRow - 1));
                }
            }
        }
        return result;
    }
}