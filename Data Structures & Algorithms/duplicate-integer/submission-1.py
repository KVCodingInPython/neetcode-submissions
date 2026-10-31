class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = HashSet()
        for i in range(len(nums)):
            if distinct_nums.contains(nums[i]):
                return True
            else:
                distinct_nums.add(nums[i])
        return False

class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = []

        for _ in range(size):
            self.buckets.append([])

    def _hash(self, value):
        return value % self.size

    def add(self, value):
        index = self._hash(value)

        for x in self.buckets[index]:
            if x == value:
                return

        self.buckets[index].append(value)

    def contains(self, value):
        index = self._hash(value)

        for x in self.buckets[index]:
            if x == value:
                return True

        return False

    def remove(self, value):
        index = self._hash(value)

        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == value:
                del bucket[i]
                return

    def print_set(self):
        print(self.buckets)



        