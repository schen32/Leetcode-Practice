class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [(0, rooms[0])]
        visited = set()
        while stack:
            room_id, keys = stack.pop()
            visited.add(room_id)
            if len(visited) == len(rooms):
                return True

            for key in keys:
                if not key in visited:
                    stack.append((key, rooms[key]))
        return False