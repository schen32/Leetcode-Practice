class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if not endGene in bank_set:
            return -1

        queue = deque([( startGene, 0 )])
        visited = { startGene }

        ch = ["A", "C", "G", "T"]

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for c in ch:
                    if gene[i] == c:
                        continue
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene in bank_set and not newGene in visited:
                        queue.append((newGene, steps + 1))
                        visited.add(newGene)
        return -1