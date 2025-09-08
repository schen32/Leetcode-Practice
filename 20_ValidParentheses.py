class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
            }

        bracketStack = []
        for bracket in s:
            if bracket in closeToOpen:
                if not bracketStack or bracketStack[-1] != closeToOpen[bracket]:
                    return False
                bracketStack.pop()
            else:
                bracketStack.append(bracket)
        
        if bracketStack:
            return False
        return True