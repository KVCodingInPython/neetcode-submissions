class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # To find anagrams we want to do this:
        # For each string in strs, find the character counts of each char and represent it in an array at each index, and if not encountered before append its character count to an array, one way is putting the combined ascii value of all chars of that word into an index in an array, and then we relate its index to index in a , where we add the array, if we see same combined ascii value of next word, we append that word with the previous word and add it to that array dynamically
         # Store an array of lists of strings that are anagrams of each other
         anagram_map = defaultdict(list)
         for s in strs:
            key = "".join(sorted(s))

            anagram_map[key].append(s)
        
         return list(anagram_map.values())
        



                    