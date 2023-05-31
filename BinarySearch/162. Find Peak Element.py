# BinarySearch - Medium
# https://leetcode.com/problems/find-peak-element/

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0]>nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1
        l = 1; r = len(nums)-2
        while l < r:
            mid = l + (r-l)//2

            # Compare the adjacent elements
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]: return mid

            # If less than the left element, then the peak must be at the left side. Same to the right part
            elif nums[mid] < nums[mid-1]: r = mid -1 
            else: l = mid + 1
        return l
    
# Main idea: Use binary search to find the peak element. 