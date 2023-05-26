# Array - Medium
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sorting method: sort the array from the ascending order and compare with the original array
        # Get the first mismatch element index and the last element index. Time: O(nlogn)
        sorted_nums = sorted(nums)
        
        l, u = len(nums) - 1,0
        for i in range(len(nums)):
            if nums[i]!=sorted_nums[i]:
                l=min(l, i)
                u=max(u, i)
         
        return 0 if l>=u else u-l+1
    
        # Two pointer: l indicates the first element starts the descending order; same to r

        l = 0; r = len(nums)-1; 
        while l < r and nums[l] <= nums[l+1]:
            l += 1

        if l == r: return 0

        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        # Need to set max and min of the selected slide window from l to r. For [1,3,2,2,2], the initial l is 1 and r is 2.
        # Need to extend the slide window to the end 
        windowMax = max(nums[l:r+1])
        windowMin = min(nums[l:r+1])

        while l > 0 and nums[l-1] > windowMin:
            l -= 1
                
        while r < len(nums)-1 and nums[r+1] < windowMax:
            r += 1

        return r - l + 1