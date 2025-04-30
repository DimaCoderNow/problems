def diagonalSum(self, mat: List[List[int]]) -> int:
    i = 0
    j = len(mat[0]) - 1
    res = 0
    while True:
        if i >= j:
            if i == j:
                res += mat[i][j]
            break
        res = res + mat[i][i] + mat[j][j] + mat[i][j] + mat[j][i]
        i += 1
        j -= 1
    return res


def diagonalSum_2(self, mat: List[List[int]]) -> int:
    res = 0
    for i in range(len(mat[0])):
        for j in range(len(mat[0])):
            if i == j or i == len(mat[0]) - j - 1:
                res += mat[i][j]
    return res
