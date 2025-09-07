class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True

            n = str(n)
            square_digits = 0
            for digit in n:
                square_digits += int(digit) ** 2
            n = square_digits
        
        return False