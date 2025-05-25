class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        matrix.reverse()
        for r in range(rows):
            for c in range(r,rows):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
