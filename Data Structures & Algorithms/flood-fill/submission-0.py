class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sol = [row[:] for row in image]
        rows, cols = len(sol), len(sol[0])
        original = sol[sr][sc]
        if original == color:
            return sol

        q = deque()
        q.append((sr, sc))
        while q:
            curr_row, curr_col = q.popleft()
            sol[curr_row][curr_col] = color

            if curr_row + 1 < rows and sol[curr_row + 1][curr_col] == original:
                q.append((curr_row + 1, curr_col))
            if curr_row - 1 >= 0 and sol[curr_row - 1][curr_col] == original:
                q.append((curr_row - 1, curr_col))
            if curr_col + 1 < cols and sol[curr_row][curr_col + 1] == original:
                q.append((curr_row, curr_col + 1))
            if curr_col - 1 >= 0 and sol[curr_row][curr_col - 1] == original:
                q.append((curr_row, curr_col - 1))

        return sol

