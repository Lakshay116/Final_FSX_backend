def solveNQueens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col):
        # base case: If all queens are placed
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append(j)
            results.append(solution)
            return True

        res = False
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                res = solve(board, col + 1) or res
                board[i][col] = 0  # backtrack

        return res

    results = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return results

# Example usage:
print(solveNQueens(4))