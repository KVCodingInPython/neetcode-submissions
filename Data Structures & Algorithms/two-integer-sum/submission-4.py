class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = dict()
        for i in range(len(nums)):
            numsMap[nums[i]] = i
        
        
        for j in range(len(nums)):
            if target - nums[j] in numsMap:
                idx = numsMap.get(target - nums[j])
                if idx == j:
                    continue
                elif idx < j:
                    return [idx, j]
                
                return [j, idx]
        
        return []
                
                

        