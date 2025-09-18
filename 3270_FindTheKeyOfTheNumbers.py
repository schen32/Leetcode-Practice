class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Pad with leading zeros
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        key_digits = []
        for i in range(4):
            # Take the smallest digit among the three
            d = min(s1[i], s2[i], s3[i])
            key_digits.append(d)

        # Build the key, remove leading zeros
        key = "".join(key_digits).lstrip("0")
        return int(key) if key else 0
