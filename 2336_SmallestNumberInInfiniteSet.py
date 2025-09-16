class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.added_back = []
        self.in_heap = set()

    def popSmallest(self) -> int:
        if self.added_back:
            res = heapq.heappop(self.added_back)
            self.in_heap.remove(res)
            return res
        else:
            self.curr += 1
            return self.curr - 1

    def addBack(self, num: int) -> None:
        if num < self.curr and not num in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)