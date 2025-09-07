class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = defaultdict(int)
        for char in s:
            charDict[char] += 1
        
        for char in t:
            charDict[char] -= 1

        for char, count in charDict.items():
            if count != 0:
                return False
        
        return True