# Array - Mediam
# https://leetcode.com/problems/sentence-similarity-iii/

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        l1 = list(sentence1.split(" "))
        l2 = list(sentence2.split(" "))

        # Return False if it is in the middle of the second array
        if len(l1) == 1:
            return True if l1[0] == l2[0] or l1[0] == l2[-1] else False
        elif len(l2) == 1:
            return True if l2[0] == l1[0] or l2[0] == l1[-1] else False
        
        while l1 and l2:
            if l1[0] == l2[0]: 
                l1.pop(0)
                l2.pop(0)
            elif l1[-1] == l2[-1]: 
                l1.pop()
                l2.pop()
            else:
                return False
        return True
    
# Main idea: Stack/Queue idea. Pop out the same element at the beginning of the two array or the end of the two array until
# one array is empty. Directly return if the length is one. 