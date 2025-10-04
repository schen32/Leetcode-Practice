class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()          # make sure fastest processors go first
        tasks.sort()                  # ascending
        minTime = float("-inf")
        index = len(tasks) - 1

        for time in processorTime:
            for i in range(4):
                minTime = max(minTime, time + tasks[index])
                index -= 1
        return minTime
