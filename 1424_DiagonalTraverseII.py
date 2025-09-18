class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal_map[i + j].append(nums[i][j])

        res = []
        for key in sorted(diagonal_map.keys()):
            res.extend(reversed(diagonal_map[key]))
        return res