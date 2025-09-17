class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        for i in range(len(word)):
            if i > 0 and word[i] == word[i - 1]:
                res += 1
        return res