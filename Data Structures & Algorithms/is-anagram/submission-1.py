class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False
        character_freq = {}

        for i in range(s_length):
            if s[i] not in character_freq:
                character_freq[s[i]] = 1
            else:
                character_freq[s[i]] += 1
        
        for i in range(t_length):
            if t[i] in character_freq:
                character_freq[t[i]] -= 1
        
        if all(val == 0 for val in character_freq.values()):
            return True
        
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

