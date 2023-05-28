# Stack - Medium
# https://leetcode.com/problems/asteroid-collision/

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        l = []
        for i in asteroids:
            # Only considers if the current item is negative. If it is negative, do a loop to compare l[-1]
            while l and i < 0 and 0 < l[-1]:
                # if i is greater than l[-1], pop out the l[-1], i to compare l[-2]
                if -i > l[-1]:
                    l.pop()
                # if both are equal, pop out l[-1] and move to the next i 
                elif -i == l[-1]: 
                    l.pop()
                    break
                else: 
                    break
            else:
                # append if it is positive or l[-1] is negative
                l.append(i)
        return l
    
# Main idea: Use Stack property. 