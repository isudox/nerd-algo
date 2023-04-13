"""1024. Video Stitching
https://leetcode.com/problems/video-stitching/

You are given a series of video clips from a sporting event that lasted time
seconds. These video clips can be overlapping with each other and have
varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and
ends at time clips[i][1]. We can cut these clips into segments freely: for
example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into
segments that cover the entire sporting event ([0, time]). If the task is
impossible, return -1.

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event
[0, 10].

Example 2:

Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation:
We can't cover [0,5] with only [0,1] and [1,2].

Example 3:

Input: clips =
[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
time = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].

Example 4:

Input: clips = [[0,4],[2,8]], time = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.

Constraints:

1 <= clips.length <= 100
0 <= clips[i][0] <= clips[i][1] <= 100
0 <= time <= 100
"""
from typing import List


class Solution:
    def video_stitching(self, clips: List[List[int]], time: int) -> int:
        """greedy"""
        def helper(left: int, right: int) -> int:
            if left >= right:
                return 0
            if not clips:
                return float('inf')
            left_len = right_len = 0
            left_idx = right_idx = -1
            for i in range(len(clips)):
                clip = clips[i]
                if clip[0] <= left and clip[1] - left > left_len:
                    left_len = clip[1] - left
                    left_idx = i
                if clip[1] >= right and right - clip[0] > right_len:
                    right_len = right - clip[0]
                    right_idx = i
            if left_idx == -1 or right_idx == -1:
                return float('inf')
            if clips[left_idx][1] >= right or clips[right_idx][0] <= left:
                return 1
            left = clips[left_idx][1]
            right = clips[right_idx][0]
            del clips[min(left_idx, right_idx)]
            del clips[max(left_idx, right_idx) - 1]
            return 2 + helper(left, right)

        ans = helper(0, time)
        return ans if ans < float('inf') else -1
