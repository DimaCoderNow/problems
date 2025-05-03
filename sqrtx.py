def mySqrt(self, x: int) -> int:
    if x == 1:
        return 1
    res = 0
    for i in range(x // 2 + 1):
        if i * i > x:
            return res
        res = int(i)
    return res
