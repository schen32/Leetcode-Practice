class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexDict = defaultdict(int)

        for i, number in enumerate(numbers):
            diff = target - number
            if diff in indexDict:
                return [indexDict[diff] + 1, i + 1]
            
            indexDict[number] = i
        
        return [-1, -1]