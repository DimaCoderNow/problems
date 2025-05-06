def sortSentence(self, s: str) -> str:
    res = [""] * 9
    for word in s.split(" "):
        index = (word[-1])
        res[int(index) - 1] = word[:-1]
    return " ".join(res).rstrip()
