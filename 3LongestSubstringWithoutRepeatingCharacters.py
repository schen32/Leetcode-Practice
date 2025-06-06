class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        substring = set()
        longestSub = 0
        while r < len(s):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longestSub = max(longestSub, len(substring))
            r += 1
        return longestSub