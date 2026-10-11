class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n 
        res[n - 1] = 1
        for i in range(n - 1, 0, -1):
            res[i-1] = nums[i] * res[i]

        curr_prod = 1
        for i in range(n):
            res[i] = curr_prod * res[i]
            curr_prod *= nums[i]

        return res
        