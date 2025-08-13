class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for index, citation in enumerate(citations):
            if citation >= index + 1:
                h = index + 1
            else:
                break
        return h