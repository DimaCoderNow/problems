def isSubsequence(self, s: str, t: str) -> bool:
    a = 0
    tmp_s = ""
    for char in t:
        if a > len(s) - 1:
            break
        if char == s[a]:
            tmp_s += char
            a += 1
    return s == tmp_s
