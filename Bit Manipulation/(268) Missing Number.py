class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Declare the lacking number variable
        missing = 0
        #Sort the array
        nums = sorted(nums)

        #Edge cases, if first element isn't 0 or the last element isn't N
        if nums[len(nums)-1] != len(nums):
            missing = len(nums)
        if nums[0] != 0:
            missing = 0



        #Looping through array and checking difference between next and current element
        #if it's 1, then check another pair, if not return missing element as: current + 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] != 1:
                missing = nums[i] + 1
        return missing