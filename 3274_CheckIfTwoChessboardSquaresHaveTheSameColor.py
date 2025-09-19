class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1 = ord(coordinate1[0]) - ord("a")
        col2 = ord(coordinate2[0]) - ord("a")
        row1 = ord(coordinate1[1]) - ord("1")
        row2 = ord(coordinate2[1]) - ord("1")

        return (row1 + col1) % 2 == (row2 + col2) % 2