class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)

        # array of len 26 to count char frequency
        # use that as a key in hashmap
        for str in strs:
            charFreq = [0] * 26

            for char in str:
                charFreq[ord(char) - ord('a')] += 1
            
            anagramGroups[tuple(charFreq)].append(str)
        
        return list(anagramGroups.values())
