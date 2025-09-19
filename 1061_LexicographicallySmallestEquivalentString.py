class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i + ord('a')): chr(i + ord('a')) for i in range(26)}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # Always keep the lexicographically smaller one as root
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry
        
        # Build equivalences
        for a, b in zip(s1, s2):
            union(a, b)
        
        # Build result
        return "".join(find(c) for c in baseStr)
