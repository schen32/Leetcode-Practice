class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if not num:
            return True
        return not (num % 10 == 0)