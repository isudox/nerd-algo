package com.leetcode;

/**
 * 1024. Video Stitching
 * https://leetcode.com/problems/video-stitching/
 *
 * You are given a series of video clips from a sporting event that lasted time
 * seconds. These video clips can be overlapping with each other and have
 * varied lengths.
 *
 * Each video clip clips[i] is an interval: it starts at time clips[i][0] and
 * ends at time clips[i][1]. We can cut these clips into segments freely: for
 * example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
 *
 * Return the minimum number of clips needed so that we can cut the clips into
 * segments that cover the entire sporting event ([0, time]). If the task is
 * impossible, return -1.
 *
 * Example 1:
 *
 * Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
 * Output: 3
 * Explanation:
 * We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
 * Then, we can reconstruct the sporting event as follows:
 * We cut [1,9] into segments [1,2] + [2,8] + [8,9].
 * Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event
 * [0, 10].
 *
 * Example 2:
 *
 * Input: clips = [[0,1],[1,2]], time = 5
 * Output: -1
 * Explanation:
 * We can't cover [0,5] with only [0,1] and [1,2].
 *
 * Example 3:
 *
 * Input: clips =
 * [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
 * time = 9
 * Output: 3
 * Explanation:
 * We can take clips [0,4], [4,7], and [6,9].
 *
 * Example 4:
 *
 * Input: clips = [[0,4],[2,8]], time = 5
 * Output: 2
 * Explanation:
 * Notice you can have extra video after the event ends.
 *
 * Constraints:
 *
 * 1 <= clips.length <= 100
 * 0 <= clips[i][0] <= clips[i][1] <= 100
 * 0 <= time <= 100
 */
class Problem1024 {

    private boolean flag = true;

    public int videoStitching(int[][] clips, int time) {
        int[] used = new int[clips.length];
        int ans = helper(clips, 0, time, used);
        return flag ? ans : -1;
    }

    private int helper(int[][] clips, int left, int right, int[] used) {
        if (left >= right) return 0;
        if (clips.length == 0) {
            flag = false;
            return -1;
        }
        int left_len = 0, right_len = 0;
        int left_idx = -1, right_idx = -1;
        for (int i = 0; i < clips.length; i++) {
            if (used[i] == 1) continue;
            int[] clip = clips[i];
            if (clip[0] <= left && clip[1] - left > left_len) {
                left_len = clip[1] - left;
                left_idx = i;
            }
            if (clip[1] >= right && right - clip[0]> right_len) {
                right_len = right - clip[0];
                right_idx = i;
            }
        }
        if (left_idx == -1 || right_idx == -1) {
            flag = false;
            return -1;
        }
        if (clips[left_idx][1] >= right || clips[right_idx][0] <= left) return 1;
        used[left_idx] = 1;
        used[right_idx] = 1;
        return helper(clips, clips[left_idx][1], clips[right_idx][0], used) + 2;
    }
}
