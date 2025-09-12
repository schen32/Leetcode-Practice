class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(path, open, close):
            if not open and not close:
                res.append(path)
                return
            
            if open:
                backtrack(path + "(", open - 1, close)
            if close > open:
                backtrack(path + ")", open, close - 1)
        backtrack("", n, n)
        return res