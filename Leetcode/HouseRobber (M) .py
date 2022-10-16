class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = nums[0]
        for i in range(1, len(nums)):
            temp = currMax 
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
        return currMax