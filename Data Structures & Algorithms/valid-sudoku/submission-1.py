class Solution:
    def checkThreeByThree(self, board: List[List[str]], start_i: int, start_j: int) -> bool:
        visited = set()
        for i in range(3):
            for j in range(3):
                curr_num = board[start_i + i][start_j + j]
                if curr_num in visited:
                    return False
                if curr_num != ".":
                    visited.add(curr_num)
        
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            visited = set()
            for j in range(len(board[i])):
                curr_num = board[i][j]
                if curr_num in visited:
                    return False
                if curr_num != ".":
                    visited.add(curr_num)
        
        for i in range(len(board)):
            visited = set()
            for j in range(len(board[i])):
                curr_num = board[j][i]
                if curr_num in visited:
                    return False
                if curr_num != ".":
                    visited.add(curr_num)
        
        return (self.checkThreeByThree(board, 0, 0) and 
        self.checkThreeByThree(board, 3, 0) and 
        self.checkThreeByThree(board, 6, 0) and 
        self.checkThreeByThree(board, 0, 3) and 
        self.checkThreeByThree(board, 3, 3) and 
        self.checkThreeByThree(board, 6, 3) and 
        self.checkThreeByThree(board, 0, 6) and 
        self.checkThreeByThree(board, 3, 6) and 
        self.checkThreeByThree(board, 6, 6))