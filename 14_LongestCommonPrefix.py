class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        commonPrefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(s) and i < len(commonPrefix) and s[i] == commonPrefix[i]:
                i += 1
            commonPrefix = commonPrefix[:i]
            if not commonPrefix:
                return ""
        return commonPrefix