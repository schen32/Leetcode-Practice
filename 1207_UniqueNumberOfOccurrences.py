class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = defaultdict(int)
        for num in arr:
            occurrences[num] += 1
        
        seen = set()
        for o in occurrences.values():
            if o in seen:
                return False
            seen.add(o)
        return True