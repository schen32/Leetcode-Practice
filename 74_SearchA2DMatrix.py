class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def searchColumns(top, bottom):
            if top > bottom:
                return False

            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                return searchColumns(top, middle - 1)
            elif matrix[middle][0] <= target <= matrix[middle][-1]:
                return searchRows(0, n - 1, middle)
            elif matrix[middle][-1] < target:
                return searchColumns(middle + 1, bottom)
        
        def searchRows(left, right, column):
            if left > right:
                return False
            
            middle = (left + right) // 2
            if target < matrix[column][middle]:
                return searchRows(left, middle - 1, column)
            elif matrix[column][middle] == target:
                return True
            elif matrix[column][middle] < target:
                return searchRows(middle + 1, right, column)

        return searchColumns(0, m - 1)