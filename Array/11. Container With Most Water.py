# Array - Medium
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vol = 0
        l = 0; r = len(height)-1
        while l < r:
            vol = max(vol,(r-l)*min(height[r],height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return vol
    
# Main idea: use two-pointer approach. Initialize a left pointer and a right pointer (based on the length of the array) 
# to iterativly find out the maximum volume (height_of_difference * length). 
# Move the left pointer to right if the left_side_height is less than the right side and vice versa.

test = Solution()
height = [1,8,6,2,5,4,8,3,7]
print (test.maxArea(height))
 

