class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Intuition:
            transpose
            reverse columnwise
        """
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Rotate column-wise
        for row in range(m):
            l, r = 0, n-1
            while l<r:
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                l+=1
                r-=1
        