from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = deque([0])
        visited = set()
        while keys:
            key = keys.popleft()
            if key in visited:
                continue
            room = rooms[key]
            keys += room
            visited.add(key)
        if len(visited) == len(rooms):
            return True
        return False
