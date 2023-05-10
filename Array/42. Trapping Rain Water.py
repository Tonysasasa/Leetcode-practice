# Array - Hard
# https://leetcode.com/problems/trapping-rain-water

class Solution(object):
    def trap(self, height):

        # Use lmax and rmax to find the number of water trapped. If the current bar is less than the max, then the 
        # max-height[i] amount of water can be trapped
        l = 0; r = len(height)-1; lmax = 0; rmax = 0
        ans = 0

        while l < r:

            # There must be a higher bar on the left, so move the right pointer to left by 1
            if height[l] > height[r]:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    ans = ans + rmax - height[r]
                r -= 1
            else:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    ans = ans + lmax - height[l]
                l += 1
        return ans
    

# Main idea: Use two-pointer appraoch. 