# BinarySearch - Easy
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0; r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return l 
    
# Closed interval [0,len(nums)]