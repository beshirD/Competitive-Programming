class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
        for left_right in range(len(board)):
            if board[left_right][0] == "O":
                self.dfs(board,left_right,0,neighbours)
            if board[left_right][len(board[0]) - 1] == "O":
                self.dfs(board,left_right,len(board[0]) - 1,neighbours)
        for top_bottom in range(len(board[0])):
            if board[0][top_bottom] == "O":
                self.dfs(board,0,top_bottom,neighbours)
            if board[len(board)-1][top_bottom] == "O":
                self.dfs(board,len(board)-1,top_bottom,neighbours)
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == 1:
                    board[row][column] = "O"
                elif board[row][column] == "O":
                    board[row][column] = "X"
        return board
    def dfs(self,board,row,col,neighbours):
        board[row][col] = 1
        for neighbour in neighbours:
            new_row = row + neighbour[0]
            new_col = col + neighbour[1]
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == "O":
                self.dfs(board,new_row,new_col,neighbours)
        