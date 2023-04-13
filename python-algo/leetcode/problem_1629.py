"""1629. Slowest Key
https://leetcode.com/problems/slowest-key/
"""
from typing import List


def slowest_key(release_times: List[int], keys_pressed: str) -> str:
    for i in range(len(release_times) - 1, 0, -1):
        release_times[i] -= release_times[i - 1]
    max_time = release_times[-1]
    ans = keys_pressed[-1]
    for i in range(len(release_times)):
        if release_times[i] > max_time:
            max_time = release_times[i]
            ans = keys_pressed[i]
        elif release_times[i] == max_time:
            ans = max(ans, keys_pressed[i])
    return ans
