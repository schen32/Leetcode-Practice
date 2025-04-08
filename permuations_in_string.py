class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = dict()
        s2count = dict()
        matches = 0

        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)

        for i in range(26):
            letter = chr(ord("a") + i)
            if letter not in s1count:
                s1count[letter] = 0
            if letter not in s2count:
                s2count[letter] = 0

            if s1count[letter] == s2count[letter]:
                matches += 1
        
        j = 0
        for i in range(len(s1), len(s2)+1):
            
            print(s2[j+1:i+1])
            if matches == 26:
                return True
            if i >= len(s2):
                break
            s2count[s2[i]] += 1
            s2count[s2[j]] -= 1

            if s2count[s2[i]] == s1count[s2[i]]:
                matches += 1
            elif s2count[s2[i]] == s1count[s2[i]] + 1:
                matches -= 1

            if s2count[s2[j]] == s1count[s2[j]]:
                matches += 1
            elif s2count[s2[j]] == s1count[s2[j]] - 1:
                matches -= 1
            j += 1
        return False
    


s1="adc"
s2="dcda"
print(s1)
print(s2)
sol = Solution()
print(sol.checkInclusion(s1, s2))
print("True")
print()

s1="abc"
s2="lecaabee"
print(s1)
print(s2)
sol = Solution()
print(sol.checkInclusion(s1, s2))
print("False")
print()



s1="ab"
s2="lecabee"
print(s1)
print(s2)
sol = Solution()
print(sol.checkInclusion(s1, s2))
print("True")
print()