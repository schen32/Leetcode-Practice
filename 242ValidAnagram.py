class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charFreqS = defaultdict(int)
        charFreqT = defaultdict(int)

        for i in range(len(s)):
            charFreqS[s[i]] += 1
            charFreqT[t[i]] += 1

        return charFreqS == charFreqT