class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixsumMat = [[0] * (cols+1) for r in range(rows+1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefixsumMat[r][c+1]
                self.prefixsumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1
        bottom_right = self.prefixsumMat[r2][c2]
        top = self.prefixsumMat[r1-1][c2]
        left = self.prefixsumMat[r2][c1-1]
        topleftcorner = self.prefixsumMat[r1-1][c1-1]
        return bottom_right - top - left + topleftcorner

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)