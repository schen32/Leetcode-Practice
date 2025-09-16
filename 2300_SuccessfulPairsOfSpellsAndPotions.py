class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()

        def search(spell):
            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        res = []
        for spell in spells:
            index = search(spell)
            res.append(m - index)
        return res