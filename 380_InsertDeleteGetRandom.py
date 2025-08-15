class RandomizedSet:

    def __init__(self):
        self.nums = list()
        self.pos = dict()

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        val_index = self.pos[val]
        last_val = self.nums[-1]

        self.nums[val_index] = last_val
        self.pos[last_val] = val_index

        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()