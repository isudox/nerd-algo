"""838. Push Dominoes
https://leetcode.com/problems/push-dominoes/
"""
import collections


def push_dominoes(dominoes: str) -> str:
    n = len(dominoes)
    arr = [0] * n
    q = collections.deque()
    for i, ch in enumerate(dominoes):
        if ch != '.':
            q.append(i)
        if ch == 'L':
            arr[i] = -1
        if ch == 'R':
            arr[i] = 1
    while q:
        i = q.popleft()
        if arr[i] < 0:  # left
            if i == 0 or arr[i - 1] != 0:
                continue
            elif i == 1:
                arr[0] = arr[i] - 1
            elif arr[i - 2] <= 0 or arr[i - 2] + arr[i] > 0:
                arr[i - 1] = arr[i] - 1
                q.append(i - 1)
        elif arr[i] > 0:
            if i == n - 1 or arr[i + 1] != 0:
                continue
            elif i == n - 2:
                arr[-1] = arr[i] + 1
            elif arr[i + 2] >= 0 or arr[i] + arr[i + 2] < 0:
                arr[i + 1] = arr[i] + 1
                q.append(i + 1)
    ans = ''
    for v in arr:
        if v == 0:
            ans += '.'
        if v > 0:
            ans += 'R'
        if v < 0:
            ans += 'L'
    return ans
