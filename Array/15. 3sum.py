# Array - Medium
# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];  
        nums = sorted(nums) # Order the array from small

        for i in range (len(nums)):            
            # The first condition is to remove the first duplicate element after the first iteration 
            # i.e. for [-1,-1, 0, 1, 2], the first [-1, 0, 1] is saved. Then i is moved from the first -1 to the second -1，
            # In this case, we need to pass i to the third element 0 to avoid the duplicate situation.

            # It also will fail if we start i from 0 (if nums[i]==nums[i+1])
            if i > 0 and nums[i-1]==nums[i]:  
                continue 

            l = i + 1; r = len(nums)-1
            while l < r:
                cur = nums[l] + nums[i] + nums[r] 
                if cur == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    # The second condition is to remove the second duplicate element. [-1, 1, 1, 1, 1, 0]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # The third condition is to remove the third duplicate element. [-1, 1, 0, 0, 0, 0]
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1                   
                    l += 1; r-= 1
                elif cur > 0:                   
                    r -= 1
                else:                   
                    l += 1
        return ans
    
# Main idea: use two-point approach. It is essential to iterate within an ordered array since we need to compare array values
# and move the pointers to right or left. 

test = Solution()
nums = [-1,0,1,2,-1,-4]
print (test.threeSum(nums))