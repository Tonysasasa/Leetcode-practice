# Array - Medium
# https://leetcode.com/problems/next-permutation

# The replacement must be in place and use only constant extra memory.

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2 # Starts from the second last element to compare with last element 
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1    

        if i >= 0:         
            j = len(nums) - 1
            while nums[i] >= nums[j]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i] # swap

        nums[i+1:] = sorted(nums[i+1:])  # reverse the order to the increasing order
        return nums

# Main idea: use two-pointer approach and backward tracking. 
test = Solution()
nums = [1,5,8,4,7,6,5,3,1]
print (test.nextPermutation(nums))
