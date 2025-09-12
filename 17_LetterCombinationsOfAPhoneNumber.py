class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        all_letters = []
        def backtrack(i, letters):
            if i == len(digits):
                all_letters.append(letters)
                return

            for letter in num_to_letter[digits[i]]:
                backtrack(i + 1, letters + letter)
        
        backtrack(0, "")
        return all_letters