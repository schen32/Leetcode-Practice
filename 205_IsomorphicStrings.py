class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = dict()
        t_to_s = dict()

        for s_char, t_char in zip(s, t):
            if s_char in s_to_t and s_to_t[s_char] != t_char:
                return False
            if t_char in t_to_s and t_to_s[t_char] != s_char:
                return False

            s_to_t[s_char] = t_char
            t_to_s[t_char] = s_char
        
        return True