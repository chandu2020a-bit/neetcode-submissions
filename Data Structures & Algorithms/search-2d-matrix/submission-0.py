class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n1, n2 = len(matrix), len(matrix[0])
        for i in range(n1):
            for j in range(n2):
                if matrix[i][j] == target:
                    return True 
        return False