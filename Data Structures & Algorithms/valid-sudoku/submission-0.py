from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                curr = board[row][col]
                if curr in rows[row] or curr in columns[col] or curr in boxes[tuple([row // 3, col // 3])]:
                    return False
                
                rows[row].add(curr)
                columns[col].add(curr)
                boxes[tuple([row // 3, col // 3])].add(curr)
        
        return True