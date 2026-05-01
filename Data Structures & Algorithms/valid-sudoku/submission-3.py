class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) # key = row, value = array
        cols = collections.defaultdict(set) # key = col, value = array
        squares = collections.defaultdict(set) # key = r // 3 col // 3. You can have tuples as keys in python.
        for r in range(9):
            for c in range(9):
                curr_value = board[r][c]


                if (curr_value in rows[r] or
                    curr_value in cols[c] or
                    curr_value in squares[(r // 3, c // 3)]):
                    return False
                
                if curr_value != ".":
                    rows[r].add(curr_value)
                    cols[c].add(curr_value)
                    squares[(r // 3, c // 3)].add(curr_value)
        
        return True

