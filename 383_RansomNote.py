class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterDict = defaultdict(int)
        for letter in ransomNote:
            letterDict[letter] += 1

        for letter in magazine:
            letterDict[letter] -= 1
        
        for letter, count in letterDict.items():
            if count > 0:
                return False
        return True