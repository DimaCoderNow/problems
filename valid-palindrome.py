def isPalindrome(self, s: str) -> bool:
    s = "".join(list(map(lambda x: x if x.isalnum() else "", s.lower())))
    if s == s[::-1]:
        return True
    return False
