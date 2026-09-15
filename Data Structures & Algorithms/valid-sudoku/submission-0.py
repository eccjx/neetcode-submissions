class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].add(num)
                    if num in cols[j]:
                        return False
                    else:
                        cols[j].add(num)
                    if num in squares[(i // 3, j // 3)]:
                        return False
                    else:
                        squares[(i // 3, j // 3)].add(num)
        return True