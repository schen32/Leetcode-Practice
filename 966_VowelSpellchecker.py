class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def mask_vowels(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())
        
        exact = set(wordlist)
        case_insensitive = {}
        vowel_error = {}
        
        for word in wordlist:
            lower = word.lower()
            masked = mask_vowels(word)
            if lower not in case_insensitive:
                case_insensitive[lower] = word
            if masked not in vowel_error:
                vowel_error[masked] = word
        
        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif mask_vowels(query) in vowel_error:
                result.append(vowel_error[mask_vowels(query)])
            else:
                result.append("")
        
        return result