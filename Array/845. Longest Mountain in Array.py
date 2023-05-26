# Array - Medium
# https://leetcode.com/problems/longest-mountain-in-array/

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3: return 0
        window = 0

        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                l = r = i
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1
                window = max(window,r-l+1)
        return window

# Main idea: use two pointers approach. Very similar to Leetcode 581. 
# For 581: it finds two indices to make a slide window (need to extend the slide window to left or right depends on the value)
# The key for this question is to find the peak in the array. For each peak find the maximum window it can take