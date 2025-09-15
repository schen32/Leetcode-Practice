class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = defaultdict(int)
        for char in word1:
            freq1[char] += 1
        
        freq2 = defaultdict(int)
        for char in word2:
            freq2[char] += 1

        # Compare character sets
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Compare frequency MULTISETS (not just sets)
        return sorted(freq1.values()) == sorted(freq2.values())