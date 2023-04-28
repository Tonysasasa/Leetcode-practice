# Array - Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array

# Must write an algorithm with O(log n) runtime complexity.

class Solution(object):
    def search(self, nums, target):
        l = 0; r = len(nums)-1; mid = (l+r)//2
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            # Find if left branch is ascending order, then do binary search again in left branch
            if nums[l] <= nums[mid]: 
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1

            # if not, do the binary search in the right branch
            else:
                if nums[mid] <= target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    
# Main idea: Binary search. Since the constraint is within O(log n) runtime complexity, we can use binary search to keep
# searching left branch and right branck with ascending order. 
# Compare to the normal binary search, it just seperates the array into two branches and do binary seach individually. 

test = Solution()
nums = [5,1,3]; target = 3
print (test.search(nums,target))
    
