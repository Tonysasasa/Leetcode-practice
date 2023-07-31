# Array - Easy
# https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for j in range(len(nums)):
            if target - nums[j] in dic and dic[target - nums[j]] != j:
                return [j,dic[target - nums[j]]]


        #for i in range (len(nums)):
            #for j in range(i+1,len(nums)):
                #if nums[i] + nums[j] == target:
                    #return [i,j]
    
# Main idea: 
# Brute force - using two loops to continuesly search nums. O(n^2)
# Advance algorithm - using python dictionary (HashTable) to store nums and their locations.   