class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for day, temp in enumerate(temperatures):            
            while stack and temp > stack[-1][1]:
                prev_day, prev_temp = stack.pop()
                res[prev_day] = day - prev_day
            stack.append((day, temp))
        return res