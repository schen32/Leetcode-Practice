class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        j = 0  # write pointer

        while i < n:
            char = chars[i]
            count = 0

            # count repeating group
            while i < n and chars[i] == char:
                i += 1
                count += 1

            # write char
            chars[j] = char
            j += 1

            # write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1

        return j
