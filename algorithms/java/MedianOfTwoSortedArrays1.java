// MedianOfTwoSortedArrays.java v1.0
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        if (m == 0 && n == 0) return 0;
        int len = m + n;
        int[] ints = new int[len];
        int i = 0, j = 0;
        for (int index = 0; index < len; index++) {
            if (i < m && j < n) {
                if (nums1[i] < nums2[j]) {
                    ints[index] = nums1[i++];
                } else {
                    ints[index] = nums2[j++];
                }
            } else {
                if (i < m) {
                    ints[index] = nums1[i++];
                }
                if (j < n) {
                    ints[index] = nums2[j++];
                }
            }
        }
        if (len % 2 == 0) {
            return (ints[len / 2 - 1] + ints[len / 2]) / 2.0;
        } else {
            return ints[len / 2];
        }
    }
}