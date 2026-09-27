
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number in the array
        frequency_counter = Counter(nums)
      
        # Get the k most common elements
        # most_common(k) returns a list of (element, count) tuples
        most_common_elements = frequency_counter.most_common(k)
      
        # Extract only the elements (not their counts) from the tuples
        result = [element for element, count in most_common_elements]
      
        return result

    