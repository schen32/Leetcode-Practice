class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        user_unique_minutes = defaultdict(set)
        for id, time, in logs:
            user_unique_minutes[id].add(time)
        
        answer = [0] * k
        for user, minutes in user_unique_minutes.items():
            answer[len(minutes) - 1] += 1
        return answer