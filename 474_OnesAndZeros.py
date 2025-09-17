class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [(s.count("0"), s.count("1")) for s in strs]
        
        memo = {}
        def backtrack(index, zeros, ones):
            if index >= len(strs):
                return 0
            if (index, zeros, ones) in memo:
                return memo[(index, zeros, ones)]
            
            res = backtrack(index + 1, zeros, ones)
            z, o = count[index]
            if zeros >= z and ones >= o:
                res = max(res, 1 + backtrack(index + 1, zeros - z, ones - o))
            memo[(index, zeros, ones)] = res
            return res
        return backtrack(0, m, n)