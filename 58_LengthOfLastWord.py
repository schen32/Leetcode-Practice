class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = False
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if start:
                    break
            else:
                if not start:
                    start = True
                count += 1
        return count