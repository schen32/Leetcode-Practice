class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = dict()
        s_to_pattern = dict()
        s_words = s.split()
        if len(pattern) != len(s_words):
            return False

        for p_char, s_word in zip(pattern, s_words):
            if p_char in pattern_to_s and pattern_to_s[p_char] != s_word:
                return False
            if s_word in s_to_pattern and s_to_pattern[s_word] != p_char:
                return False

            pattern_to_s[p_char] = s_word
            s_to_pattern[s_word] = p_char

        return True