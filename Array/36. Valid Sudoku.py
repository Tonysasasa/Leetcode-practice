# Array - Medium
# https://leetcode.com/problems/valid-sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]

                # check if it is a valid number
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
    

# Main idea: use tuple property - [int, str], [str, int], [int, int, str] are three different types of tuples. 
# Only compare the same type of tuple if the number of the tuples are same len() vs len(set())

test = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print (test.isValidSudoku(board))