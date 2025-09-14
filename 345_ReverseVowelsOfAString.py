class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = { "a", "e", "i", "o", "u" }
        s_list = list(s)
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].lower() not in vowel_set:
                left += 1
            elif s[right].lower() not in vowel_set:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)