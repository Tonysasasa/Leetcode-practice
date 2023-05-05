# Array - Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Sliding window appraoch - worst case O(n)
        l = []; f = 0; s = 0
        while s < len(nums):
            if nums[s] == target:
                l.append(s)
                f = s+1
                while f < len(nums) and nums[f] == target:
                    f += 1
                l.append(f-1)
                return l
            else:
                s += 1
        return [-1,-1]
    
    # Binary search approach - seperate to find the two indices of starting point and the end point. 
    def searchRange(self, nums, target):
        result = [-1, -1]        
        result[0] = self.findStartingIndex(nums, target)  
        result[1] = self.findEndingIndex(nums, target)       
        return result 

    def findStartingIndex(self, nums, target):
        index = -1 
        low, high = 0, len(nums) -1 
        
        while low <= high: 
            mid = low + (high - low)/2 			
            if nums[mid] == target: 
                index = mid 
                high = mid - 1 
            elif nums[mid] > target:  
                high = mid - 1 
            else: 
                low = mid + 1              
        return index
  
    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) -1
        
        while low <= high:           
            mid = low + (high - low)/2           
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target: 
                high = mid - 1
            else:
                 low = mid + 1     
        return index
    
test = Solution()
nums = [1,1,1,2,2,4,4,8,8]; target = 2
print (test.searchRange(nums,target))