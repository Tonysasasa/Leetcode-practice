# Array - Medium
# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0 ; j = 0; s= 0; ans = float('inf')
        for j in range(len(nums)):
            s = s + nums[j]
            while s >= target:
                ans = min(ans,j-i+1)
                s = s - nums[i]
                i += 1
        if ans != float('inf'):
            return ans
        else:
            return 0

# Main idea: Use slide window approach. Start with right pointer to enlarge the window until it reaches/exceeds target.