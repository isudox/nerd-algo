"""841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""
from typing import List


class Solution:
    def can_visit_all_rooms(self, rooms: List[List[int]]) -> bool:
        def dfs(key: int):
            nonlocal count
            count += 1
            opened.add(key)
            for k in rooms[key]:
                if k not in opened:
                    dfs(k)

        opened = set()
        count = 0
        dfs(0)
        return count == len(rooms)

    def can_visit_all_rooms_1(self, rooms: List[List[int]]) -> bool:
        opened = [0]
        queue = [0]
        count = 0
        while queue:
            count += 1
            i = queue.pop(0)
            for key in rooms[i]:
                if key not in opened:
                    opened.append(key)
                    queue.append(key)
        return count == len(rooms)

    def can_visit_all_rooms_2(self, rooms: List[List[int]]) -> bool:
        opened = [0]
        keys = rooms[0]
        while keys:
            new_keys = []
            for key in keys:
                if key not in opened:
                    new_keys.extend(rooms[key])
                    opened.append(key)
                keys = new_keys

        return len(opened) == len(rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        q = rooms[0]
        visited[0] = True
        while q:
            n = len(q)
            for _ in range(n):
                k = q.pop(0)
                if not visited[k]:
                    q += rooms[k]
                    visited[k] = True
        for v in visited:
            if not v:
                return False
        return True
