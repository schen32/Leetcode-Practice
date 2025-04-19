class Solution:
    def isValid(self, s: str) -> bool:
        valid = { "(": ")", "{": "}", "[": "]" }
        stack = []
        for bracket in s:
            if bracket in valid:
                stack.append(bracket)
            else:
                if not stack or valid[stack[-1]] != bracket:
                    return False
                stack.pop()
        if stack:
            return False
        return True