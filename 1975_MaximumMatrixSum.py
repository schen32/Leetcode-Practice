class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float("inf")
        num_negs = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = matrix[i][j]
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    num_negs += 1
        
        if num_negs % 2 == 0:
            return total
        else:
            return total - 2 * min_abs