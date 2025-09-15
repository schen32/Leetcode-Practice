class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0
        vowel_set = { "a", "e", "i", "o", "u" }
        num_vowels = 0
        while right < k:
            if s[right] in vowel_set:
                num_vowels += 1
            right += 1
        max_vowels = num_vowels

        while right < len(s):
            if s[right] in vowel_set:
                num_vowels += 1
            if s[left] in vowel_set:
                num_vowels -= 1
            left += 1
            right += 1
            max_vowels = max(max_vowels, num_vowels)
        return max_vowels