def guessNumber(self, n: int) -> int:
    a = 1
    b = n        
    while a <= b:
        midl = (a + b)//2
        tmp = guess(midl)
        if tmp == 0:
            return midl
        elif tmp == -1:
            b = midl - 1
        else:
            a = midl + 1
